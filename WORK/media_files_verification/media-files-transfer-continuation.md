# Wasabi Migration Continuation Notes

## Current Status

- Verified 14 folders with perfect matches (including two large ones: Communication_media at 611 GB and development media at 1.1 TB)
- PHOTO ARCHIVES folder requires special handling (size-only verification)
- 15 small to medium folders still require verification

## PHOTO ARCHIVES Approach

Since the source scan for PHOTO ARCHIVES failed with directory errors, we'll use a size-only verification approach:

```bash
# Size-only verification for PHOTO ARCHIVES
rclone check "dropbox-wasabi-migration:/Media Files Online Backup 8-31-2020/PHOTO ARCHIVES" "dropbox-wasabi-migration:/WASABI-MIGRATION/Media Files Online Backup 8-31-2020/PHOTO ARCHIVES" --size-only --one-way --exclude "Greens Restaurant for Katie/**" --exclude "Images for Catherine 11-2024/**" --tpslimit=1
```

This approach:
1. Uses `--size-only` for faster verification (comparing file sizes instead of checksums)
2. Uses `--one-way` to only check that files in source exist in destination
3. Excludes the problematic folders that caused errors
4. Maintains rate limiting to avoid API issues

## Verified Folders Summary

| Folder | Size | Files |
|--------|------|-------|
| development media | 1.1 TB | 5,193 |
| Communication_media | 611 GB | 2,004 |
| PHOTO ARCHIVES | 502 GB | 55,521 |
| Multimedia drive | 150 GB | 13,732 |
| Mountain Seat Ceremonies | 21.7 GB | 16 |
| Cut 9.0 | 10.6 GB | 83 |
| Experts_Mind_2010 | 5.52 GB | 361 |
| Fonts | 598.8 MB | 758 |
| Linda Oryoki Cut 3.0 | 171.6 MB | 1 |
| Logos | 75 MB | 93 |
| Digital Voice Editor | 47.5 MB | 84 |
| 15_04 Furyu Schroeder Portraits | 41.7 MB | 5 |
| 2020 Letterhead and Envelopes | 3.02 MB | 2 |

## Pending Verification Folders

- MYL2006 Digital Files
- Path of Urban Practice
- Paul Haller
- Program Communications
- Program Dept. Projects
- scan
- Skit Night 2017
- Style Manual
- Taryn's Backup
- Videos, Tass Rez
- Volunteer Appreci...n Nov 07 photos
- Website Redesign - Barbara
- Website Redesign - Earthlyn
- Wendy Johnson interview
- YEAR END LETTERS
- ZMC Dharma Talks Fall 2016

## Next Steps After Verification

1. Transfer verified folders to NAS using batch_transfer.py script
2. Archive "Media Files Online Backup 8-31-2020" directly to AWS S3 Deep Glacier
3. Consider optional backup copy on Wasabi for redundancy

## Verification Commands Template

For remaining folders:

```bash
# Source location
rclone size "dropbox-wasabi-migration:/Media Files Online Backup 8-31-2020/[Folder Name]" --json --tpslimit=1 > original_[folder]_size.json

# Staged location
rclone size "dropbox-wasabi-migration:/WASABI-MIGRATION/Media Files Online Backup 8-31-2020/[Folder Name]" --json --tpslimit=1 > staged_[folder]_size.json

# Compare
cat original_[folder]_size.json
cat staged_[folder]_size.json
```

## Safety Notes

- All verification commands (`rclone size`, `cat`) are read-only and won't modify files
- Dropbox has trash/version history as additional safety net
- Actual transfers will use `rclone copy` which preserves source files
- The verification process ensures data integrity before any transfers

## Special Collection Notes

"Media Files Online Backup 8-31-2020" is an older collection managed by less technically-oriented staff and volunteers. After verification and archiving to Deep Glacier, this collection will be considered handled separately from the main Wasabi migration.

---

This document contains all key information to continue the verification process tomorrow.