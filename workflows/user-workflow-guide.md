# User Workflow Guide

**Version:** 1.0  
**Last Updated:** March 25, 2025  
**Purpose:** Instructions for users during media storage migration

## Migration Phases Overview

This guide explains what you need to do during each phase of our migration from Dropbox to the new Wasabi storage system. Please read the instructions for your current migration phase carefully.

## Phase 1: Pre-Migration (Current)

During this phase, we're setting up the new storage system while you continue to work as normal.

### Your Responsibilities

1. **Continue using Dropbox as normal** for all your daily work.

2. **Copy files for migration:**
   - Identify files you want migrated
   - Copy them to the "WASABI-MIGRATION" folder
   - Organize them into appropriate subfolders
   - DO NOT modify these files once copied

3. **Document your workflows:**
   - Complete the Use Case form sent to you
   - Note any special requirements for your files
   - Identify mission-critical assets

4. **Prepare for new tools:**
   - Schedule your training session
   - Review preliminary guides
   - Install Cyberduck/Mountain Duck when requested

### What to Expect

- No changes to your daily workflow yet
- Periodic updates about migration progress
- IT will be transferring and verifying content behind the scenes
- You'll be contacted to schedule training

## Phase 2: Parallel Operation

During this phase, you'll start using the new storage system for new content while still accessing existing content in Dropbox.

### Setting Up Your Access

1. **Install Cyberduck/Mountain Duck:**
   - Download from the link provided in your email
   - Install with default settings
   - Input the credentials provided to you

2. **Configure your connection:**
   - Create a new bookmark with these settings:
     - Protocol: S3
     - Server: s3.wasabi.com
     - Port: 443
     - Access Key ID: [your provided key]
     - Secret Access Key: [your provided key]
     - Path: [your department folder]
   - Save the bookmark with a descriptive name
   - Test the connection

### New File Storage Process

1. **For NEW content:**
   - Use Cyberduck/Mountain Duck to upload
   - Save to the appropriate dated folder:
     - "2024_Active_Projects"
     - "2024_Dharma_Talks"
     - "2024_Online_Programs"
   - Follow the new file naming convention:
     - Format: YYYY-MM-DD_ProjectName_FileDescription
     - Example: 2025-03-25_SpringRetreat_PromotionalImage.jpg

2. **For EXISTING content:**
   - Continue accessing through Dropbox
   - Files remain read-only in Dropbox
   - Request help if you need to modify existing files

### Sharing Files

1. **Internal sharing:**
   - Share the Wasabi file path with colleagues
   - They can access with their own credentials

2. **External sharing:**
   - Use the "Generate Temporary URL" feature in Cyberduck
   - Right-click file → Copy URL → Set expiration time
   - Share the generated link

### Getting Help

- Daily office hours: 10-11 AM via Google Meet
- Email support: storage-migration@sfzc.org
- Emergency assistance: IT help desk ext. 4587
- Google Chat: "DAM: Wasabi migration" space

## Phase 3: Post-Migration

Once all files have been migrated and verified, we'll complete the transition to the new storage system.

### Your Responsibilities

1. **Verify your files:**
   - Confirm all needed files are available in Wasabi
   - Check a sample of files to ensure they open correctly
   - Report any missing or corrupted files immediately

2. **Update your workflows:**
   - Update all saved links and references
   - Modify any scripts or tools to point to new storage
   - Update bookmarks in all applications

3. **Complete final training:**
   - Attend advanced feature training
   - Learn about version history and recovery
   - Understand backup procedures

4. **Clean up Dropbox:**
   - Once everything is verified, delete your Dropbox files
   - Update any external sharing links

### What to Expect

- Full access to all files in Wasabi
- Automated backups (no user action required)
- Improved storage capacity and performance
- Continued support as needed

## File Naming and Organization Standards

### Standard File Naming Convention

```
YYYY-MM-DD_ProjectName_FileDescription.ext
```

Examples:
- 2025-03-25_SpringRetreat_PromotionalImage.jpg
- 2025-03-26_DharmaTalk_AudioRecording.mp3
- 2025-03-28_ZenCenter_BudgetReport.xlsx

### Folder Structure

```
Department/
├── YYYY_Active_Projects/
│   ├── ProjectName1/
│   └── ProjectName2/
├── YYYY_Archive/
│   ├── MonthName/
│   └── ProjectName/
└── YYYY_Templates/
```

### Important Guidelines

- Use underscores (_) instead of spaces
- Include the date at the beginning for easy sorting
- Use descriptive but concise file names
- Keep folder structures shallow (max 3-4 levels)
- Avoid special characters (#, %, &, etc.)

## Cyberduck/Mountain Duck Usage

### Basic Operations

**Connect to storage:**
1. Open Cyberduck
2. Double-click your saved bookmark
3. Enter password if prompted

**Upload files:**
1. Drag and drop files from your computer
2. Or use the "Upload" button in the toolbar
3. Wait for upload to complete before closing

**Download files:**
1. Select the file(s) you need
2. Right-click and select "Download"
3. Choose destination folder

**Create folders:**
1. Click the "New Folder" button in toolbar
2. Name according to naming conventions
3. Press Enter to create

### Advanced Features

**Version history (Wasabi):**
1. Right-click a file
2. Select "Versions"
3. View or restore previous versions

**Generate temporary links:**
1. Right-click a file
2. Select "Copy URL"
3. Configure expiration time and permissions
4. Share the URL

**Synchronize folders:**
1. In Mountain Duck, right-click a folder
2. Select "Synchronize"
3. Choose direction and options
4. Start synchronization

## Troubleshooting Common Issues

### Cannot Connect

1. Check your internet connection
2. Verify your credentials are correct
3. Try restarting Cyberduck/Mountain Duck
4. Contact IT if problems persist

### Slow Uploads/Downloads

1. Check your internet connection
2. Try reducing the number of simultaneous transfers:
   - Preferences → Transfers → Connections: set to 1
3. For large files, use Mountain Duck instead of Cyberduck

### File Not Found

1. Check the file path carefully
2. Verify permissions with IT
3. Check if the file is in transition (being migrated)

### Error Messages

**"Access Denied":**
- Check permissions with IT
- Verify you're using the correct credentials

**"Operation Timed Out":**
- Check network connection
- Try again later (possible congestion)
- Break large transfers into smaller batches

**"File Already Exists":**
- Use a different filename
- Or choose "Replace" if you want to overwrite

## Getting Support

### When to Contact IT

- Missing files after migration
- Permission issues accessing content
- Errors that persist after troubleshooting
- Questions about workflow changes

### How to Report Issues

1. Screenshot any error messages
2. Note exact steps to reproduce the issue
3. Include file paths and names
4. Send to storage-migration@sfzc.org
5. For urgent issues: IT help desk ext. 4587

### Training Resources

- Video tutorials: [Link to internal site]
- Quick reference guides: [Link to internal site]
- Weekly webinars: Thursdays 2-3 PM
- Personal assistance: By appointment

## Timeline and Next Steps

1. **March 2025**
   - Install Cyberduck/Mountain Duck
   - Complete basic training

2. **April 2025**
   - Begin using Wasabi for new content
   - Continue accessing existing content in Dropbox

3. **May 2025**
   - Complete verification of migrated content
   - Full transition to Wasabi
   - Cleanup of Dropbox content

We appreciate your patience and cooperation during this transition. If you have any questions or concerns, please don't hesitate to reach out to the migration team.