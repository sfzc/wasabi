#!/usr/bin/env python3
"""
Storage Migration: Batch Transfer Script

Version: 4.0
Date: March 25, 2025
Author: Greg Bilke

This script performs safe batch transfers from Dropbox to Synology NAS with:
- Command preview before execution
- Clean progress display (4-line status area)
- Full verification after transfer
- Comprehensive logging and error handling

SAFETY FEATURES:
- Only uses 'copy' command (never sync, move, or delete)
- Only targets the WASABI-MIGRATION folder
- Performs verification after each transfer
- Requires explicit confirmation before execution
- Preserves source files
"""

import argparse
import subprocess
import os
import time
import datetime
import json
import sys
import shutil  # For getting terminal size
import socket  # For hostname
import re      # For parsing output

# SAFETY: Configuration - NEVER modify these paths
SOURCE_BASE = "dropbox-wasabi-migration:/WASABI-MIGRATION"
DEST_BASE = "DS423:/Backups/WASABI-MIGRATION"

# Terminal Colors
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# Setup argument parser
def parse_arguments():
    parser = argparse.ArgumentParser(description='Safely transfer files from Dropbox to Synology NAS')
    parser.add_argument('folders', nargs='+', help='Folder(s) to transfer (must be in WASABI-MIGRATION)')
    parser.add_argument('--subpath', default='', help='Subpath within WASABI-MIGRATION (e.g., "Media Files Online Backup 8-31-2020")')
    parser.add_argument('--transfers', type=int, default=4, help='Number of concurrent transfers (default: 4)')
    parser.add_argument('--checkers', type=int, default=8, help='Number of checkers (default: 8)')
    parser.add_argument('--tpslimit', type=int, default=2, help='Transactions per second limit (default: 2)')
    parser.add_argument('--bwlimit', default='10M', help='Bandwidth limit (default: 10M)')
    parser.add_argument('--no-verify', action='store_true', help='Skip verification step')
    parser.add_argument('--yes', action='store_true', help='Skip confirmation prompts')
    parser.add_argument('--dry-run-only', action='store_true', help='Only perform dry run, no actual transfer')
    
    return parser.parse_args()

# Setup logging
def setup_logging():
    log_dir = "logs"
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    main_log = f"{log_dir}/transfer_batch_{timestamp}.log"
    
    # Create a hostname identifier for log uniqueness
    hostname = socket.gethostname().replace(" ", "-")
    
    return log_dir, main_log, timestamp, hostname

# Write to both console and log file
def log_message(message, main_log, also_print=True, level="INFO"):
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    # Format based on level
    if level == "INFO":
        prefix = Colors.BLUE + "[INFO]" + Colors.END
    elif level == "WARNING":
        prefix = Colors.YELLOW + "[WARNING]" + Colors.END
    elif level == "ERROR":
        prefix = Colors.RED + "[ERROR]" + Colors.END
    elif level == "SUCCESS":
        prefix = Colors.GREEN + "[SUCCESS]" + Colors.END
    else:
        prefix = "[" + level + "]"
    
    log_line = f"{timestamp} - {prefix} {message}"
    
    with open(main_log, "a", encoding="utf-8") as f:
        # Strip colors for log file
        clean_line = re.sub(r'\033\[\d+m', '', log_line)
        f.write(f"{clean_line}\n")
    
    if also_print:
        print(log_line)

# Print safety banner
def print_safety_banner(main_log):
    log_message("\n" + "="*80, main_log)
    log_message(Colors.BOLD + "SAFETY CHECK - This script will ONLY:" + Colors.END, main_log)
    log_message("1. Copy files from Dropbox to Synology NAS", main_log)
    log_message("2. Only target the WASABI-MIGRATION folder", main_log)
    log_message("3. Only use the safe 'copy' command (never sync, move, or delete)", main_log)
    log_message("4. Run in DRY RUN mode first for safety", main_log)
    log_message("5. Verify all transfers with checksums where possible", main_log)
    log_message("=" * 80 + "\n", main_log)

# Check if paths are within allowed scope
def validate_paths(folders, subpath, main_log):
    # SAFETY: Ensure we're only working with WASABI-MIGRATION folder
    if subpath and (subpath.startswith("/") or ".." in subpath):
        log_message(f"FATAL: Subpath '{subpath}' contains disallowed path characters", main_log, level="ERROR")
        return False
        
    # Construct the full paths
    full_source_base = f"{SOURCE_BASE}/{subpath}" if subpath else SOURCE_BASE
    full_dest_base = f"{DEST_BASE}/{subpath}" if subpath else DEST_BASE
    
    for folder in folders:
        if "/" in folder or ".." in folder or folder.startswith("."):
            log_message(f"FATAL: Folder name '{folder}' contains disallowed path characters", main_log, level="ERROR")
            return False
    
    # Additional validation
    for path in [full_source_base, full_dest_base]:
        if "WASABI-MIGRATION" not in path:
            log_message(f"FATAL: Path '{path}' is outside the allowed WASABI-MIGRATION root", main_log, level="ERROR")
            return False
    
    return True, full_source_base, full_dest_base

# Format file size for human readability
def format_size(size_bytes):
    if size_bytes < 1024:
        return f"{size_bytes} bytes"
    elif size_bytes < 1024 * 1024:
        return f"{size_bytes/1024:.2f} KB"
    elif size_bytes < 1024 * 1024 * 1024:
        return f"{size_bytes/(1024*1024):.2f} MB"
    else:
        return f"{size_bytes/(1024*1024*1024):.2f} GB"

# Main function
def main():
    args = parse_arguments()
    log_dir, main_log, timestamp, hostname = setup_logging()
    
    # Print banner
    print_safety_banner(main_log)
    
    # SAFETY: Validate paths
    result = validate_paths(args.folders, args.subpath, main_log)
    if not result:
        sys.exit(1)
    else:
        valid, full_source_base, full_dest_base = result
    
    # Log script execution
    log_message(f"Starting batch transfer script v4.0 on {hostname}", main_log)
    log_message(f"Command: {' '.join(sys.argv)}", main_log)
    
    # Verify basic access before proceeding
    try:
        log_message("Checking source access...", main_log)
        subprocess.run(["rclone", "lsd", SOURCE_BASE.split(":")[0] + ":"], check=True, capture_output=True)
        log_message("Source remote accessible", main_log)
        
        log_message("Checking destination access...", main_log)
        subprocess.run(["rclone", "lsd", DEST_BASE.split(":")[0] + ":"], check=True, capture_output=True)
        log_message("Destination remote accessible", main_log)
    except subprocess.CalledProcessError as e:
        log_message(f"ACCESS ERROR: {str(e)}", main_log, level="ERROR")
        log_message("Cannot access remotes, aborting for safety.", main_log, level="ERROR")
        sys.exit(1)
    
    # Get terminal dimensions for progress display
    try:
        terminal_width = shutil.get_terminal_size().columns
    except:
        terminal_width = 80  # Default width if unable to determine
    
    # Process each folder in the list
    for folder in args.folders:
        folder_start_time = time.time()
        folder_log = f"{log_dir}/{folder.replace(' ', '_')}-{timestamp}.log"
        
        log_message("\n" + "="*80, main_log)
        log_message(f"STARTING PROCESS FOR: {folder}", main_log)
        log_message("="*80, main_log)
        
        # Create destination directory if it doesn't exist
        try:
            mkdir_cmd = ["rclone", "mkdir", f"{full_dest_base}/{folder}"]
            subprocess.run(mkdir_cmd, check=True, capture_output=True)
            log_message(f"Destination folder created/verified: {folder}", main_log)
        except subprocess.CalledProcessError as e:
            log_message(f"ERROR creating destination folder: {str(e)}", main_log, level="ERROR")
            log_message("Skipping this folder for safety.", main_log, level="WARNING")
            continue
        
        # Check source folder contents
        try:
            # Get folder size first
            size_cmd = ["rclone", "size", f"{full_source_base}/{folder}", "--json"]
            size_result = subprocess.run(size_cmd, check=True, capture_output=True, text=True)
            
            # Parse JSON response
            try:
                size_data = json.loads(size_result.stdout)
                total_bytes = size_data.get("bytes", 0)
                total_count = size_data.get("count", 0)
            except json.JSONDecodeError as e:
                log_message(f"WARNING: Could not parse folder size information: {str(e)}", main_log, level="WARNING")
                log_message("Proceeding with transfer anyway.", main_log, level="WARNING")
                total_bytes = 0
                total_count = 0
            
            # Log the folder size
            log_message(f"Folder contains {total_count} files totaling {format_size(total_bytes)}", main_log)
            
            # DRY RUN first
            log_message(f"\nStarting DRY RUN for {folder}...", main_log)
            dry_run_cmd = [
                "rclone", "copy",
                f"{full_source_base}/{folder}",
                f"{full_dest_base}/{folder}",
                "--dry-run",
                "--progress",
                "--checksum",
                f"--transfers={args.transfers}",
                f"--checkers={args.checkers}",
                f"--tpslimit={args.tpslimit}", 
                f"--bwlimit={args.bwlimit}",
                "--stats=15s"
            ]
            
            log_message(f"Command: {' '.join(dry_run_cmd)}", main_log)
            dry_run = subprocess.run(dry_run_cmd, capture_output=True, text=True)
            
            # Log the dry run output
            log_message("\n--- DRY RUN OUTPUT ---", main_log, also_print=False)
            with open(folder_log, "a", encoding="utf-8") as f:
                f.write("\n--- DRY RUN OUTPUT ---\n")
                f.write(dry_run.stdout)
                if dry_run.stderr:
                    f.write("\nERRORS:\n")
                    f.write(dry_run.stderr)
                f.write("\n--- END DRY RUN OUTPUT ---\n")
            
            # Show a summary
            if "Transferred:" in dry_run.stdout:
                transfer_lines = [line for line in dry_run.stdout.split("\n") if "Transferred:" in line and "ETA" in line]
                if transfer_lines:
                    log_message(f"Dry run summary: {transfer_lines[-1]}", main_log)
            
            log_message("DRY RUN completed - NO FILES WERE TRANSFERRED", main_log)
            log_message("Review the logs in the 'logs' folder carefully.", main_log)
            
            # If dry-run-only flag is set, skip the actual transfer
            if args.dry_run_only:
                log_message(f"Skipping actual transfer for {folder} (--dry-run-only specified)", main_log)
                continue
            
            # Ask for confirmation unless --yes was specified
            if not args.yes:
                proceed = input(f"\nDo you want to proceed with the actual transfer of '{folder}'? (yes/no): ")
                log_message(f"User chose to {'proceed' if proceed.lower() == 'yes' else 'cancel'} the transfer.", main_log)
                
                if proceed.lower() != "yes":
                    log_message(f"Skipping actual transfer for {folder} based on user decision", main_log)
                    continue
            
            log_message(f"\nSTARTING ACTUAL TRANSFER for {folder}...", main_log)
            
            # Build the actual transfer command (remove --dry-run)
            actual_cmd = [
                "rclone", "copy",
                f"{full_source_base}/{folder}",
                f"{full_dest_base}/{folder}",
                "--progress",
                "--checksum",
                f"--transfers={args.transfers}",
                f"--checkers={args.checkers}",
                f"--tpslimit={args.tpslimit}",
                f"--bwlimit={args.bwlimit}",
                "--stats=15s",
                f"--log-file={folder_log}"
            ]
            
            log_message(f"Command: {' '.join(actual_cmd)}", main_log)
            
            try:
                # Better progress monitoring with cleaner display
                log_message("Starting transfer process...", main_log)
                log_message("Progress updates will appear below (press Ctrl+C to stop):", main_log)
                print()  # Extra line before progress begins
                
                # Use subprocess.Popen to capture output in real-time
                process = subprocess.Popen(
                    actual_cmd,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.STDOUT,
                    text=True,
                    bufsize=1,
                    universal_newlines=True
                )
                
                # Print only the most recent status, overwriting previous output
                # Create a 4-line status display area
                print("\n\n\n\n")  # 4 blank lines
                
                try:
                    for line in iter(process.stdout.readline, ''):
                        line = line.rstrip()
                        if line:
                            # Log all lines to file
                            with open(folder_log, "a", encoding="utf-8") as f:
                                f.write(line + "\n")
                            
                            # Only display status lines with progress info
                            if ("Transferred:" in line or "Transferring:" in line or 
                                "Elapsed time:" in line or line.strip().startswith("*")):
                                
                                # Move up 4 lines
                                sys.stdout.write('\033[4A')
                                # Clear lines
                                sys.stdout.write('\033[J')
                                
                                # Create a 4-line status block
                                lines = []
                                if "Transferred:" in line and "ETA" in line:
                                    lines.append(f"Status: {line}")
                                elif "Transferred:" in line:
                                    lines.append(f"Files: {line}")
                                elif "Elapsed time:" in line:
                                    lines.append(f"Time: {line}")
                                elif "Transferring:" in line:
                                    lines.append("Current files:")
                                elif line.strip().startswith("*"):
                                    # Format current file info
                                    file_info = line.strip()
                                    # Truncate if too long for display
                                    if len(file_info) > terminal_width - 3:
                                        file_info = file_info[:terminal_width - 6] + "..."
                                    lines.append(f"  {file_info}")
                                
                                # Print status block
                                for status_line in lines[:4]:  # Limit to 4 lines
                                    print(status_line)
                                
                                # Fill any remaining lines with blanks
                                for _ in range(4 - len(lines)):
                                    print()
                                
                                # Flush output
                                sys.stdout.flush()
                except:
                    # If any errors with display, fall back to basic logging
                    log_message("Advanced display error. Check log file for progress.", main_log, level="WARNING")
                    # Continue reading output to capture in log
                    for line in iter(process.stdout.readline, ''):
                        with open(folder_log, "a", encoding="utf-8") as f:
                            f.write(line)
                
                # Wait for the process to complete
                process.wait()
                
                # Move past the status display
                print("\n\n\n")
                
                if process.returncode == 0:
                    log_message("Transfer completed successfully", main_log, level="SUCCESS")
                else:
                    log_message(f"Transfer process exited with code: {process.returncode}", main_log, level="WARNING")
                
                # Skip verification if requested
                if args.no_verify:
                    log_message("Skipping verification (--no-verify specified)", main_log)
                else:
                    # Verification step
                    log_message("\nStarting verification...", main_log)
                    verify_cmd = [
                        "rclone", "check",
                        f"{full_source_base}/{folder}",
                        f"{full_dest_base}/{folder}",
                        "--one-way"
                    ]
                    
                    log_message(f"Verification command: {' '.join(verify_cmd)}", main_log)
                    verify_result = subprocess.run(verify_cmd, capture_output=True, text=True)
                    
                    # Log verification results
                    with open(folder_log, "a", encoding="utf-8") as f:
                        f.write("\n--- VERIFICATION RESULTS ---\n")
                        f.write(verify_result.stdout)
                        if verify_result.stderr:
                            f.write("\nVERIFICATION ERRORS:\n")
                            f.write(verify_result.stderr)
                        f.write("\n--- END VERIFICATION RESULTS ---\n")
                    
                    if "0 differences found" in verify_result.stdout or verify_result.returncode == 0:
                        log_message("Verification passed - All files match", main_log, level="SUCCESS")
                    else:
                        log_message("Verification found differences, check the log file", main_log, level="ERROR")
                
            except KeyboardInterrupt:
                log_message("\nTransfer interrupted by user (Ctrl+C)", main_log, level="WARNING")
                log_message("The transfer can be resumed by running the same command again.", main_log)
                log_message("Rclone will skip files that have already been transferred.", main_log)
            except Exception as e:
                log_message(f"Error during transfer: {str(e)}", main_log, level="ERROR")
            
            # Calculate and log timing
            folder_duration = time.time() - folder_start_time
            minutes, seconds = divmod(folder_duration, 60)
            hours, minutes = divmod(minutes, 60)
            
            log_message(f"\nTime taken: {int(hours)}h {int(minutes)}m {int(seconds)}s", main_log)
            if total_bytes > 0 and folder_duration > 0:
                transfer_rate = total_bytes / folder_duration / (1024 * 1024)  # MB/s
                log_message(f"Average transfer rate: {transfer_rate:.2f} MB/s", main_log)
        
        except Exception as e:
            log_message(f"Unexpected error processing folder {folder}: {str(e)}", main_log, level="ERROR")
            log_message("Continuing to next folder for safety.", main_log, level="WARNING")

    log_message("\n" + "="*80, main_log)
    log_message("ALL FOLDERS PROCESSED", main_log)
    log_message("=" * 80, main_log)
    log_message(f"Log files are available in the '{log_dir}' directory", main_log)
    log_message("Please document these transfers in your migration dashboard", main_log)
    
    # Return success
    return 0

if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)