- # Storage Migration Dashboard

  **Version:** 2.1  
  **Last Updated:** March 27, 2025  
  **Status:** Active Migration  
  **Completion:** 18% (based on transferred data volume)

  ## Project Summary

  | Metric                | Value                               | Status        |
  | --------------------- | ----------------------------------- | ------------- |
  | Total Data Volume     | 19 TB approx                        |               |
  | Data Transferred      | 6.25 TB                             | 🟨 In Progress |
  | Collections Completed | 1/?                                 | 🟨 In Progress |
  | User Training         | TBA                                 | 🟨 In Progress |
  | AWS Configuration     | Setup                               | 🟨 In Progress |
  | NAS Configuration     | Initial population - Auto-transfers | 🟨 In Progress |
  | Wasabi Configuration  | TBA                                 | 🟨 In Progress |

  ## Migration Progress

  ### Completed Transfers

  | Source | Size                  | Files   | Transfer Date | NAS Verified   | AWS Verified | Notes |
  | ------ | --------------------- | ------- | ------------- | -------------- | ------------ | ----- |
  | ✅      | Engage Wisdom Archive | 6.25 TB | 39,795        | Mar 7-12, 2025 | ✅            | ✅     |

  ### In-Progress Transfers

  | Source | Size                                | Files | Status       | Start Date   | Expected Completion | Notes                               |
  | ------ | ----------------------------------- | ----- | ------------ | ------------ | ------------------- | ----------------------------------- |
  | 🔄      | Media Files Online Backup 8-31-2020 | TBD   | Verification | Mar 27, 2025 | TBD                 | Initial size/structure verification |

  ## Infrastructure Status

  | Component                  | Status        | Details                             | Notes                        |
  | -------------------------- | ------------- | ----------------------------------- | ---------------------------- |
  | Wasabi Setup               | 🟥 Not Started | Has not started                     |                              |
  | NAS Configuration          | 🟨 In Progress | Initial population - Auto-transfers | 12TB used of 80TB capacity   |
  | AWS S3 Setup               | 🟨 In Progress | Basic configuration complete        | Lifecycle rules pending      |
  | Automation                 | 🟨 In Progress | Wasabi → NAS working                | NAS → AWS pending            |
  | rclone Configuration       | 🟢 Complete    | All remotes configured              | Migration script operational |
  | Mountain Duck Distribution | 🟨 In Progress | 15/38 users configured              | Standard bookmarks created   |

  ## Issue Tracking

  ### Active Issues

  | ID   | Issue                     | Impact | Status        | Resolution Plan                |
  | ---- | ------------------------- | ------ | ------------- | ------------------------------ |
  | #023 | Dropbox API rate limiting | Medium | 🟨 In Progress | Implemented tpslimit parameter |

  ### Resolved Issues

  | ID   | Issue                       | Impact | Resolution                | Date Resolved |
  | ---- | --------------------------- | ------ | ------------------------- | ------------- |
  | #016 | NAS connection timeout      | High   | Increased timeout setting | Mar 15, 2025  |
  | #018 | File permission errors      | Medium | Updated SMB configuration | Mar 17, 2025  |
  | #022 | Wasabi bucket configuration | Low    | Enabled versioning        | Mar 20, 2025  |

  ## Risk Assessment

  | Risk                                 | Likelihood | Impact | Mitigation                          |
  | ------------------------------------ | ---------- | ------ | ----------------------------------- |
  | Network interruption during transfer | Medium     | Medium | Resume capability in rclone         |
  | User error deleting source files     | Low        | High   | Read-only access during migration   |
  | Verification failures                | Medium     | Medium | Multiple verification methods       |
  | Cost overruns                        | Low        | Medium | Regular monitoring of storage usage |
  | Timeline slippage                    | Medium     | Low    | Prioritization of critical content  |

  ## "Media Files Online Backup 8-31-2020" Size Verification

  Current status: Validating folder sizes and file counts between original and staged copies

  | Subfolder                           | Original Size | Original Files | Staged Size | Staged Files | Size Match | Files Match | Notes                          |
  | ----------------------------------- | ------------- | -------------- | ----------- | ------------ | ---------- | ----------- | ------------------------------ |
  | 15_04 Furyu Schroeder Portraits     | 41.7 MB       | 5              | 41.7 MB     | 5            | ✓          | ✓           | Perfect match                  |
  | 2020 Letterhead and Envelopes       | 3.02 MB       | 2              | 3.02 MB     | 2            | ✓          | ✓           | Perfect match                  |
  | Communication_media                 | 611 GB        | 2,004          | 611 GB      | 2,004        | ✓          | ✓           | Perfect match - Large folder   |
  | Cut 9.0                             | 10.6 GB       | 83             | 10.6 GB     | 83           | ✓          | ✓           | Perfect match                  |
  | development media                   | 1.1 TB        | 5,193          | 1.1 TB      | 5,193        | ✓          | ✓           | Perfect match - Large folder   |
  | Digital Voice Editor                | 47.5 MB       | 84             | 47.5 MB     | 84           | ✓          | ✓           | Perfect match                  |
  | Experts_Mind_2010                   | 5.52 GB       | 361            | 5.52 GB     | 361          | ✓          | ✓           | Perfect match                  |
  | Fonts                               | 598.8 MB      | 758            | 598.8 MB    | 758          | ✓          | ✓           | Perfect match                  |
  | Linda Oryoki Cut 3.0                | 171.6 MB      | 1              | 171.6 MB    | 1            | ✓          | ✓           | Perfect match                  |
  | Logos                               | 75 MB         | 93             | 75 MB       | 93           | ✓          | ✓           | Perfect match                  |
  | Mountain Seat Ceremonies            | 21.7 GB       | 16             | 21.7 GB     | 16           | ✓          | ✓           | Perfect match                  |
  | Multimedia drive                    | 150 GB        | 13,732         | 150 GB      | 13,732       | ✓          | ✓           | Perfect match                  |
  | MYL2006 Digital Files               |               |                |             |              |            |             | Verification pending           |
  | Path of Urban Practice              |               |                |             |              |            |             | Verification pending           |
  | Paul Haller                         |               |                |             |              |            |             | Verification pending           |
  | PHOTO ARCHIVES                      | ERROR         | ERROR          | 502 GB      | 55,521       | ?          | ?           | Using size-only check tomorrow |
  | Program Communications              |               |                |             |              |            |             | Verification pending           |
  | Program Dept. Projects              |               |                |             |              |            |             | Verification pending           |
  | scan                                |               |                |             |              |            |             | Verification pending           |
  | Skit Night 2017                     |               |                |             |              |            |             | Verification pending           |
  | Style Manual                        |               |                |             |              |            |             | Verification pending           |
  | Taryn's Backup                      |               |                |             |              |            |             | Verification pending           |
  | Videos, Tass Rez                    |               |                |             |              |            |             | Verification pending           |
  | Volunteer Appreci...n Nov 07 photos |               |                |             |              |            |             | Verification pending           |
  | Website Redesign - Barbara          |               |                |             |              |            |             | Verification pending           |
  | Website Redesign - Earthlyn         |               |                |             |              |            |             | Verification pending           |
  | Wendy Johnson interview             |               |                |             |              |            |             | Verification pending           |
  | YEAR END LETTERS                    |               |                |             |              |            |             | Verification pending           |
  | ZMC Dharma Talks Fall 2016          |               |                |             |              |            |             | Verification pending           |

  ## Next Steps

  - [ ] Continue verification of remaining folders in "Media Files Online Backup 8-31-2020"
  - [ ] Transfer verified folders to NAS using batch_transfer.py script
  - [ ] Develop special procedure for PHOTO ARCHIVES folder
  - [ ] Implement Wasabi bucket versioning for data protection
  - [ ] Consider archiving "Media Files Online Backup 8-31-2020" directly to AWS S3 Deep Glacier after verification
  - [ ] Consider optional backup copy on Wasabi for redundancy

  ## Notes & Updates

  **March 27, 2025**: Verification of "Media Files Online Backup 8-31-2020" shows 14 folders with perfect matches between source and staged locations. PHOTO ARCHIVES scan failed with directory errors - will use size-only verification tomorrow. Other folders pending verification.

  **March 25, 2025**: Started migration of Online Videos collection. Initial transfer speed is good at ~15 MiB/s.

  **March 23, 2025**: Completed development media migration with zero verification issues. Added to dashboard.

  **March 22, 2025**: Updated batch transfer script with improved progress monitoring and error handling.

  **March 18, 2025**: Multimedia drive and Program Communications transfers completed successfully.

  **March 17, 2025**: Photo Archives migration completed and verified.

  **March 12, 2025**: Engage Wisdom Archive migration completed with full verification.

  ## Legend

  - ✅ = Completed and verified
  - 🔄 = In progress
  - ⏱️ = Scheduled/Pending
  - 🟢 = Complete
  - 🟨 = In Progress
  - 🟥 = Not Started
  - ❗ = Issue/Attention Required
  - ✓ = Match
  - ✗ = Mismatch