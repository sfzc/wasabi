AUTHORITATIVE REFERENCE DOCUMENT

**Version:** 2.0
**Last Updated:** March 25, 2025
**Document Owner:** Greg Bilke, Web Operations Systems Manager (greg.bilke@sfzc.org)
**Communication Channel:** Google Chat - Spaces - DAM: Wasabi migration

## PROJECT OVERVIEW

The San Francisco Zen Center (SFZC) Digital Asset Management (DAM) migration project involves transferring approximately 19.5TB of media assets from multiple sources to a more sustainable cloud storage architecture with reliable backup and archiving capabilities.

### DATA SOURCES AND VOLUMES

| Source | Size | Files | Status |
|--------|------|-------|--------|
| **Dropbox** | | | |
| - Media Files Online Backup | 7.3TB | ~96,000 files | Pending migration |
| - User/Project Collections | 5.0TB | ~35,700 files | Pending migration |
| **Photo Archives** | 500GB | ~510,000 files | Pending migration |
| **Engage Wisdom Archive** | 6.25TB | ~39,795 files | **COMPLETED** |

**Note:** The Engage Wisdom Archive was initially documented as 7TB based on contractor inventory, but actual used space was verified at 6.25TB.

## FINALIZED ARCHITECTURE

### THREE-TIER STORAGE SOLUTION

1. **Primary Storage: Wasabi Cloud Storage**
   - Main repository replacing Dropbox
   - Direct user access via Cyberduck/Mountain Duck
   - Active files for daily operations

2. **Backup Layer: Synology DS423 NAS**
   - **STATUS: Installed and operational**
   - Automated backups from Wasabi
   - No direct user access
   - Intermediary for AWS archiving
   - Local copy for faster recovery if needed

3. **Archive Layer: AWS S3 Deep Glacier**
   - Long-term preservation
   - Lowest cost for rarely accessed files
   - Automated transfers via NAS
   - **STATUS: Configuration complete**

## MIGRATION APPROACH

The finalized migration approach consists of these steps:

1. **Initial Migration: Dropbox → Wasabi**
   - Create a designated "WASABI-MIGRATION" folder in Dropbox
   - Users place files for migration in this folder
   - Direct transfer using rclone with batch_transfer.py script
   - Full verification with checksums
   - No modification of source files until verified

2. **Backup Configuration: Wasabi → NAS**
   - Automated backups using Synology Cloud Sync
   - Regular integrity checks
   - Off-hours scheduling to minimize impact

3. **Archive Configuration: NAS → AWS Deep Glacier**
   - Uses Synology Hyper Backup for transfers
   - Deep Glacier storage class for cost optimization
   - Monthly full backups with appropriate retention

## TOOL SELECTION

### PRIMARY MIGRATION TOOLS

- **Dropbox → Wasabi**: rclone with batch_transfer.py script
- **User Access to Wasabi**: Cyberduck/Mountain Duck
- **Wasabi → NAS Backup**: Synology Cloud Sync
- **NAS → AWS Archive**: Synology Hyper Backup

### COMPLETED MIGRATIONS

- **External HDD → NAS**: Completed using ChronoSync
  - Transfer of Engage Wisdom Archive (6.25TB)
  - Full verification completed
  - Process documented for reference purposes

## TRANSFER COMMANDS REFERENCE

### SMALL FOLDERS (< 1 GB)
```
rclone copy "dropbox-wasabi-migration:/WASABI-MIGRATION/[path]" "DS423:Backups/WASABI-MIGRATION/[path]" --progress --checksum --stats=15s --log-file=[folder]-transfer.log
```

### MEDIUM FOLDERS (1-100 GB)
```
rclone copy "dropbox-wasabi-migration:/WASABI-MIGRATION/[path]" "DS423:Backups/WASABI-MIGRATION/[path]" --progress --checksum --transfers=2 --checkers=4 --tpslimit=4 --stats=15s --log-file=[folder]-transfer.log
```

### LARGE FOLDERS (>100 GB)
```
rclone copy "dropbox-wasabi-migration:/WASABI-MIGRATION/[path]" "DS423:Backups/WASABI-MIGRATION/[path]" --progress --checksum --transfers=3 --checkers=6 --tpslimit=3 --log-file=[folder]-transfer.log --stats=15s --retries=3 --timeout=120s
```

### VERIFICATION COMMAND
```
rclone check "dropbox-wasabi-migration:/WASABI-MIGRATION/[path]" "DS423:Backups/WASABI-MIGRATION/[path]" --one-way
```

## HARDWARE DECISIONS

### NAS SELECTION: SYNOLOGY DS423

- **STATUS: Purchased, installed, and operational**
- 4 drive bays (80TB maximum capacity)
- 2GB RAM
- Sufficient for automated backup operations
- Selected over DS923+ based on:
  - Cost efficiency ($399 vs $600)
  - Adequate performance for backup operations
  - No direct user interaction needed
  - Provides 2.5x more storage than previous DS220j

## PERFORMANCE METRICS

Based on initial transfers, expect the following performance:

- **Large files (videos, etc.)**: 7-15 MiB/s
- **Small files (images, documents)**: 0.5-2 MiB/s
- **Mixed content**: ~2 MiB/s average
- **Completion Times**:
  - Small folders (<100 MB): Minutes
  - Medium folders (1-50 GB): Hours
  - Large folders (>100 GB): Days

## KEY LEARNINGS

1. **SIZE DISCREPANCIES**: Significant differences between Dropbox's displayed folder sizes and actual transferred sizes have been observed. For example, Taryn's Backup showed as ~265-398MB in Dropbox but transferred 8.111 GiB (30x larger).

2. **FILE COUNT LIMITATIONS**: Both Dropbox and rclone may display a limit of 25,000 files in summary reports, but transfers can still complete successfully beyond this limit.

3. **RATE LIMITING**: Dropbox API has rate limits that can trigger "too_many_requests" errors. Use `--tpslimit=3` or lower to manage these limits. For very large folders, consider lower transfer concurrency.

4. **BATCH PROCESSING**: The batch_transfer.py script has proven effective for managing transfers with proper safety controls:
   - Dry-run verification
   - Automatic pause between operations
   - Full logging and error handling
   - Post-transfer verification

5. **VERIFICATION IMPORTANCE**: Due to the discovered discrepancies, thorough verification after each transfer is essential, including checking both file counts and content integrity.

## DATA SAFETY & VERIFICATION

### SAFETY PROTOCOLS

1. Source files remain untouched until:
   - Destination files are fully verified
   - Checksums are confirmed
   - Sample testing is completed

2. Verification occurs at multiple levels:
   - During transfer (rclone --checksum)
   - Post-transfer verification
   - Regular automated integrity checks

3. Backup Redundancy:
   - Primary storage (Wasabi)
   - Local copy (NAS)
   - Archival storage (AWS)

### VERIFICATION FRAMEWORK

For each transfer, follow this verification process:

1. **Check transfer completion status** in logs
2. **Verify file counts** match between source and destination
3. **Perform rclone check** with `--one-way` flag
4. **Test sample files** from different folders/directories 
5. **Document verification results** in the migration dashboard

## USER TRANSITION STRATEGY

### PHASED APPROACH

1. **Pre-Migration:**
   - Users continue with Dropbox
   - Backend preparation and testing
   
   **User Responsibilities:**
   - Copy files they want migrated to the designated "WASABI-MIGRATION" folder on Dropbox
   - Complete Use Case forms to document current workflows and requirements
   - Prepare for upcoming training on new tools

   **IT Team Responsibilities:**
   - Create "WASABI-MIGRATION" folder on Dropbox
   - Manage the migration from transfer folder to Wasabi
   - Verify transferred files
   - Delete files from transfer folder after verification

2. **Parallel Operation:**
   - New files to Wasabi via Cyberduck/Mountain Duck
   - Read-only access to existing files in Dropbox
   - Training and support provided
   
   **User Responsibilities:**
   - Use Cyberduck/Mountain Duck to access Wasabi storage
   - Follow new file naming conventions
   - Report issues via Google Chat Spaces "DAM: Wasabi migration"
   - Continue to access existing files on Dropbox as needed
   
   **IT Team Responsibilities:**
   - Provide user training on new tools
   - Monitor storage usage and performance
   - Address issues reported by users
   - Complete remaining migrations

3. **Post-Migration:**
   - Full Wasabi access
   - Dropbox access discontinued (except for specific collaboration needs)
   - Ongoing support as needed
   
   **User Responsibilities:**
   - Verify their migrated files (verification protocol to be developed)
   - Use Wasabi as primary storage for all new work
   - Complete required training on new workflows
   - Delete Dropbox files when ready
   
   **IT Team Responsibilities:**
   - Ensure all automation is functioning properly
   - Provide ongoing support
   - Monitor system performance
   - Document new procedures and workflows

**Note:** Some users will maintain limited Dropbox usage for external collaboration purposes, as Wasabi does not provide equivalent collaboration features.

## TROUBLESHOOTING REFERENCE

1. **Path Formatting Issues**:
   - Always use quotes around paths with spaces
   - Use forward slashes in paths, even in PowerShell

2. **Rate Limiting Errors**:
   - "too_many_requests" indicates Dropbox throttling
   - Reduce `--tpslimit` parameter (try 2 or 1)
   - Implement longer pauses between batch operations
   - Schedule large transfers during off-hours

3. **Interrupted Transfers**:
   - Simply run the same command again
   - rclone will skip already transferred files
   - Transfers will resume automatically

4. **Verification Failures**:
   - Investigate discrepancies systematically
   - Check for hidden files or resource forks
   - Review error logs for specific file issues
   - Re-run verification with `--one-way --size-only` first to identify issues

## PROJECT TIMELINE

- **Current Phase:** Dropbox → Wasabi migration (restarting with optimized process)
- **Estimated Duration:** 10-12 weeks total
- **Key Milestones:**
  1. Infrastructure setup (COMPLETED)
  2. Initial batch transfers (IN PROGRESS)
  3. User training (SCHEDULED)
  4. Parallel operation (SCHEDULED)
  5. Final verification (PLANNED)

## DOCUMENTATION MAINTENANCE

This document will be updated regularly as the project progresses. All updates must be approved by the Document Owner. When referencing information contained in this document, always verify you are using the most current version.

---

**NOTE:** This document will be updated as the project progresses. Always refer to this document for the most current project information.

## DOCUMENT CHANGE LOG

| Version | Date | Changes | Updated By |
|---------|------|---------|------------|
| 1.0 | March 8, 2025 | Initial creation of authoritative document | Greg Bilke |
| 2.0 | March 25, 2025 | Major revision incorporating learnings; restart of Dropbox migration | Greg Bilke |