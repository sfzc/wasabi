# Complete Guide: Wasabi Migration Knowledge Base Management

**Version:** 1.0
**Last Updated:** 2025-03-26
**Updated By:** Greg Bilke

## Overview

This document provides a comprehensive guide to managing the Wasabi migration knowledge base for San Francisco Zen Center. It covers the entire process from initial setup to day-to-day operations with emphasis on verification procedures and data safety.

## Table of Contents

1. [Project Context](#project-context)
2. [Knowledge Base Strategy](#knowledge-base-strategy)
3. [GitHub Integration Setup](#github-integration-setup)
4. [Claude Project Configuration](#claude-project-configuration)
5. [File Structure and Organization](#file-structure-and-organization)
6. [Versioning and Documentation Standards](#versioning-and-documentation-standards)
7. [Day-to-Day Operations](#day-to-day-operations)
8. [Safety Protocols](#safety-protocols)
9. [Troubleshooting](#troubleshooting)
10. [Appendices](#appendices)

## Project Context

The San Francisco Zen Center (SFZC) Wasabi migration project involves transferring approximately 19.5TB of media assets from multiple sources to a more sustainable cloud storage architecture with reliable backup and archiving capabilities.

### Three-Tier Storage Solution

1. **Primary Storage: Wasabi Cloud Storage**
   - Main repository replacing Dropbox
   - Direct user access via Cyberduck/Mountain Duck

2. **Backup Layer: Synology DS423 NAS**
   - Automated backups from Wasabi
   - No direct user access
   - Intermediary for AWS archiving

3. **Archive Layer: AWS S3 Deep Glacier**
   - Long-term preservation
   - Lowest cost for rarely accessed files
   - Automated transfers via NAS

### Knowledge Base Objectives

1. Maintain single source of truth for all project documentation
2. Track migration progress and issues
3. Document scripts, commands, and procedures
4. Enable easy access to all team members
5. Preserve version history for all documentation
6. Support user training and transition

## Knowledge Base Strategy

After evaluating different options, we've selected a GitHub-Claude integrated approach to maintain our knowledge base. This provides:

1. **Robust version control** through Git
2. **Centralized documentation** in a GitHub repository 
3. **AI-enhanced assistance** through Claude
4. **Structured organization** with clear folder hierarchy
5. **Universal access** for technical and non-technical staff

This approach ensures all project participants have access to up-to-date documentation while maintaining a complete history of changes.

## GitHub Integration Setup

### Step 1: Create GitHub Account

1. If you don't have a GitHub account:
   - Visit [GitHub.com](https://github.com)
   - Click "Sign up" and follow prompts
   - Use your work email (@sfzc.org)
   - Enable two-factor authentication (2FA) for security

### Step 2: Install Git

For Windows 11:

1. **Download Git installer**:
   - Visit https://git-scm.com/download/win
   - Download will start automatically 

2. **Run the installer**:
   - Accept license agreement
   - Select components:
     - Windows Explorer integration
     - Git Bash and Git GUI
     - Git LFS (Large File Support)
     - Associate Git configuration files with default editor
     - Associate .sh files with Bash
     - Add Git Bash Profile to Windows Terminal

3. **Configure installation**:
   - Choose default editor
   - Adjust PATH environment (recommended: Git from Command Prompt)
   - Configure line ending conversions (recommended: Checkout Windows-style, commit Unix-style)
   - Configure terminal emulator (MinTTY recommended)
   - Configure extra options (default options recommended)

4. **Verify installation**:
   - Open PowerShell in Windows Terminal
   - Run: `git --version`
   - Should display: `git version 2.49.0.windows.1` or similar

For macOS:

1. **Install via package manager (recommended)**:
   - Open Terminal
   - Install Homebrew if not installed: `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`
   - Install Git: `brew install git`

2. **Verify installation**:
   - Run: `git --version`
   - Should display Git version information

### Step 3: Configure Git

1. **Set user information**:
   ```
   git config --global user.name "Greg Bilke"
   git config --global user.email "greg.bilke@sfzc.org"
   ```

2. **Verify configuration**:
   ```
   git config --list
   ```

### Step 4: Create Repository

1. **Log in to GitHub**

2. **Create new repository**:
   - Click "+" icon in top-right corner
   - Select "New repository"
   - Name: `SFZC-Wasabi-Migration`
   - Description: "Wasabi storage migration project for San Francisco Zen Center"
   - Visibility: Private (recommended)
   - Initialize with README: Yes
   - Add .gitignore: Choose "Python"
   - Click "Create repository"

### Step 5: Clone Repository

1. **Copy repository URL**:
   - On repository page, click green "Code" button
   - Copy HTTPS URL

2. **Clone repository locally**:
   - Open PowerShell in Windows Terminal (or Terminal on macOS)
   - Navigate to desired location: `cd C:\path\to\projects` (Windows) or `cd ~/path/to/projects` (macOS)
   - Clone repository: `git clone https://github.com/yourusername/SFZC-Wasabi-Migration.git`
   - Enter GitHub credentials when prompted

### Step 6: Set Up Repository Structure

1. **Create folder structure**:
   ```
   cd SFZC-Wasabi-Migration
   mkdir documentation scripts logs workflows dashboard
   ```

2. **Create README files for each folder**:
   - Create README.md in each directory explaining its purpose
   - Example for documentation folder:
   ```markdown
   # Documentation

   This folder contains authoritative reference documents for the SFZC Wasabi migration project.

   ## Files

   - `authoritative-reference-document.md`: Primary project reference
   - `github-claude-kb-setup.md`: Knowledge base setup guide
   ```

## Claude Project Configuration

### Step 1: Create Claude Project

1. **Access Claude**:
   - Log in to [Claude.ai](https://claude.ai)
   - Navigate to "Projects" in left sidebar

2. **Create new project**:
   - Click "New Project"
   - Name: "SFZC Wasabi Migration"
   - Description: "Wasabi storage migration for San Francisco Zen Center"
   - Click "Create"

### Step 2: Connect GitHub Repository

1. **Find integration settings**:
   - In project view, locate "Connect" or "Integrations" in right sidebar
   - Click "Add GitHub Repository" or "Connect GitHub"

2. **Authenticate with GitHub**:
   - Follow prompts to authorize Claude to access GitHub
   - Review permissions and approve

3. **Select repository**:
   - Choose "SFZC-Wasabi-Migration" from repository list
   - Configure to access main branch
   - Click "Connect" or "Add" to finalize

### Step 3: Add Initial Knowledge Base Files

1. **Add core project files to GitHub repository**:
   - Copy `authoritative-reference-document.md` to `documentation/` folder
   - Copy `batch-transfer-script.py` to `scripts/` folder
   - Copy `project-dashboard.md` to `dashboard/` folder
   - Copy `user-workflow-guide.md` to `workflows/` folder

2. **Update file headers with version information**:
   ```markdown
   # [Document Title]
   **Version:** 1.0
   **Last Updated:** 2025-03-26
   **Updated By:** Greg Bilke
   ```

3. **Add changelog sections**:
   ```markdown
   ## Changelog

   ### v1.0 (2025-03-26)
   - Initial document creation
   ```

4. **Commit and push files**:
   ```
   git add .
   git commit -m "Initial commit: Adding core DAM migration project files"
   git push origin main
   ```

5. **Sync with Claude**:
   - In Claude project, click "Sync" or "Refresh" button
   - Verify files appear in knowledge base

## File Structure and Organization

### Core Knowledge Base Files

1. **Authoritative Reference Document**:
   - Location: `documentation/authoritative-reference-document.md`
   - Purpose: Single source of truth for project
   - Content: Overall architecture, decisions, procedures

2. **Project Dashboard**:
   - Location: `dashboard/project-dashboard.md`
   - Purpose: Track migration progress and status
   - Content: Current metrics, completed transfers, issues

3. **Batch Transfer Script**:
   - Location: `scripts/batch-transfer-script.py`
   - Purpose: Safe migration of assets
   - Content: Python script with safety protocols

4. **User Workflow Guide**:
   - Location: `workflows/user-workflow-guide.md`
   - Purpose: Instructions for end users
   - Content: Migration phases, procedures, contacts

### Additional Documentation

1. **Knowledge Base Setup Guide**:
   - Location: `documentation/github-claude-kb-setup.md`
   - Purpose: Document KB configuration
   - Content: This document

2. **Transfer Logs**:
   - Location: `logs/YYYY-MM-DD-transfer-log.md`
   - Purpose: Document individual transfers
   - Content: Commands, verification results, issues

3. **Meeting Notes**:
   - Location: `documentation/meetings/YYYY-MM-DD-meeting-notes.md`
   - Purpose: Track decisions and action items
   - Content: Attendees, discussion points, actions

## Versioning and Documentation Standards

### Versioning Convention

1. **Version numbering**:
   - Format: X.Y (Major.Minor)
   - Major (X): Significant rewrites or structural changes
   - Minor (Y): Content additions or small changes

2. **File headers**:
   ```markdown
   # [Document Title]
   **Version:** 1.0
   **Last Updated:** 2025-03-26
   **Updated By:** Greg Bilke
   ```

3. **Changelog maintenance**:
   ```markdown
   ## Changelog

   ### v1.1 (2025-03-28)
   - Added new section on verification procedures
   - Updated transfer rates based on recent tests

   ### v1.0 (2025-03-26)
   - Initial document creation
   ```

### Documentation Standards

1. **Markdown formatting**:
   - Use headers (# for main title, ## for sections)
   - Use bulleted lists for items without sequence
   - Use numbered lists for sequential steps
   - Use code blocks for commands and scripts
   - Use tables for structured data

2. **Safety emphasis**:
   - Highlight safety considerations in dedicated sections
   - Use **bold** for critical warnings
   - Include verification steps with every procedure

3. **File naming convention**:
   - Use lowercase with hyphens for spaces
   - Include dates in ISO format (YYYY-MM-DD)
   - Be descriptive but concise

## Day-to-Day Operations

### Updating Documentation

1. **Local workflow**:
   - Pull latest changes: `git pull origin main`
   - Edit files locally
   - Update version and timestamp
   - Add changelog entry
   - Commit and push: 
     ```
     git add .
     git commit -m "Update: [Brief description]"
     git push origin main
     ```

2. **GitHub web interface workflow**:
   - Navigate to file on GitHub
   - Click pencil icon to edit
   - Make changes
   - Update version and timestamp
   - Add changelog entry
   - Commit directly to main branch with descriptive message

3. **Syncing with Claude**:
   - Before each new conversation, click "Sync" in Claude
   - This ensures Claude has latest documentation

### Working with Claude

1. **Starting new chat sessions**:
   - Begin with: "Has there been any update to [filename]?"
   - This ensures you're working with latest information

2. **Generating new content**:
   - Ask Claude to create content based on existing knowledge
   - Have Claude generate in artifacts
   - Download artifacts and add to repository

3. **Updating existing documents**:
   - Ask Claude to suggest updates based on new information
   - Request changes in artifact format
   - Review, modify if needed, then add to repository

### Safety Verification Procedures

1. **Document each transfer**:
   - Create dated log in `logs/` folder
   - Record command used
   - Document verification steps
   - Note any issues encountered

2. **Verification checklist**:
   - File count matches between source and destination
   - Checksums verified with `rclone check`
   - Sample files tested from different folders
   - Log files reviewed for errors

3. **Regular integrity checks**:
   - Schedule weekly verification of transferred content
   - Update dashboard with verification status
   - Document any discrepancies found

## Safety Protocols

### Core Safety Principles

1. **Transfer operations**:
   - ONLY use "rclone copy" (never sync, move, or delete)
   - ONLY target the "WASABI-MIGRATION" folder
   - ALWAYS run "--dry-run" first for new operations
   - ALWAYS verify transfers with "rclone check"
   - NEVER modify source files until verified

2. **Storage protection**:
   - Enable versioning on all Wasabi buckets
   - Configure read-only access for most users
   - Implement graduated verification protocols

3. **Documentation of commands**:
   - Document all commands before execution
   - Paste exact commands used into logs
   - Note any deviations from standard procedures

### Batch Transfer Operation Workflow

1. **Preparation**:
   - Identify folders to transfer
   - Document in dashboard as "Scheduled"
   - Verify source and destination paths

2. **Dry run**:
   - Execute transfer with --dry-run flag
   - Review output for any issues
   - Confirm expected file counts and sizes

3. **Actual transfer**:
   - Execute transfer command
   - Monitor progress
   - Log start and completion times

4. **Verification**:
   - Check transfer logs for errors
   - Run `rclone check` for verification
   - Test sample files
   - Update dashboard with results

5. **Documentation**:
   - Update project dashboard
   - Create detailed transfer log
   - Commit changes to knowledge base

## Troubleshooting

### Common Issues

1. **Git authentication failures**:
   - Check GitHub credentials
   - Verify network connectivity
   - Consider using a personal access token

2. **Claude can't find updated information**:
   - Verify files properly committed to GitHub
   - Check that repository was synced in Claude
   - Confirm correct file paths and names

3. **Rclone transfer errors**:
   - "too_many_requests" - reduce --tpslimit parameter
   - Connection timeouts - adjust --timeout parameter
   - Verification failures - check for hidden files

### Knowledge Base Management Issues

1. **Multiple file versions in Claude**:
   - If not using GitHub integration, delete old file versions
   - Use consistent file names
   - Maintain version information in documents

2. **Merge conflicts in Git**:
   - Pull latest changes before editing
   - Resolve conflicts by editing affected files
   - Commit resolved files

3. **Missing documentation**:
   - Check all repository folders
   - Verify correct branch
   - Search for files by content

## Appendices

### A: GitHub Glossary

- **Repository**: Storage location for project files
- **Commit**: Saved change to files
- **Branch**: Parallel version of repository
- **Pull**: Get latest changes from remote repository
- **Push**: Send local changes to remote repository
- **Clone**: Create local copy of repository

### B: Markdown Quick Reference

```markdown
# Heading 1
## Heading 2
### Heading 3

**Bold text**
*Italic text*

- Bullet point
- Another bullet

1. Numbered item
2. Second item

[Link text](URL)

`inline code`

```code block```

| Column 1 | Column 2 |
|----------|----------|
| Cell 1   | Cell 2   |
```

### C: Command Reference

#### Git Commands

```
# Basic operations
git clone [repository-url]
git pull origin main
git add .
git commit -m "Commit message"
git push origin main

# Status and information
git status
git log
git diff

# Branch management
git branch
git checkout -b [new-branch-name]
git merge [branch-name]
```

#### Rclone Commands

```
# Dry run transfer
rclone copy "dropbox-wasabi-migration:/WASABI-MIGRATION/[path]" "DS423:Backups/WASABI-MIGRATION/[path]" --dry-run --progress --checksum

# Actual transfer
rclone copy "dropbox-wasabi-migration:/WASABI-MIGRATION/[path]" "DS423:Backups/WASABI-MIGRATION/[path]" --progress --checksum --transfers=4 --checkers=8 --tpslimit=2 --bwlimit=10M --stats=15s --log-file=[folder]-transfer.log

# Verification
rclone check "dropbox-wasabi-migration:/WASABI-MIGRATION/[path]" "DS423:Backups/WASABI-MIGRATION/[path]" --one-way
```

## Changelog

### v1.0 (2025-03-26)
- Initial comprehensive guide creation
- Complete end-to-end documentation of KB management process
- Detailed safety protocols and verification procedures
- Command reference and troubleshooting sections
