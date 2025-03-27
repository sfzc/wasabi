# Storage Migration Dashboard

**Version:** 2.0  
**Last Updated:** March 25, 2025  
**Status:** Active Migration  
**Completion:** 18% (based on transferred data volume)

## Project Summary

| Metric | Value | Status |
|--------|-------|--------|
| Total Data Volume | 19.5 TB | |
| Data Transferred | 3.5 TB | 🟨 In Progress |
| Collections Completed | 2/3 | 🟨 In Progress |
| User Training | 4/8 departments | 🟨 In Progress |
| AWS Configuration | Setup | 🟨 In Progress |
| NAS Configuration | Complete | 🟢 Complete |
| Wasabi Configuration | Complete | 🟢 Complete |

## Migration Progress

### Completed Transfers

| Source | Size | Files | Transfer Date | NAS Verified | AWS Verified | Notes |
|--------|------|-------|--------------|--------------|--------------|-------|
| ✅ | Engage Wisdom Archive | 6.25 TB | 39,795 | Mar 7-12, 2025 | ✅ | ✅ | Zero verification issues |
| ✅ | Photo Archives | 502 GB | 55,521 | Mar 15-17, 2025 | ✅ | - | Completed in 1d12h40m |
| ✅ | Multimedia drive | 150 GB | 13,732 | Mar 18, 2025 | ✅* | - | 1 verification issue (resource fork file) |
| ✅ | Program Communications | 115 GB | 25,000+ | Mar 18-19, 2025 | ✅ | - | Reporting capped at 25K files |
| ✅ | development media | 1.1 TB | 5,193 | Mar 22, 2025 | ✅ | - | Zero differences found |

### In-Progress Transfers

| Source | Size | Files | Status | Start Date | Expected Completion | Notes |
|--------|------|-------|--------|------------|---------------------|-------|
| 🔄 | Online Videos | 4.2 TB | ~8,700 | 15% | Mar 23, 2025 | Mar 30, 2025 | Speed: ~15 MiB/s |
| 🔄 | Dharma Talks | 3.5 TB | ~15,300 | 10% | Mar 24, 2025 | Apr 2, 2025 | Speed: ~10 MiB/s |

### Scheduled Transfers

| Source | Size | Files | Priority | Scheduled Start | Dependencies |
|--------|------|-------|----------|----------------|--------------|
| ⏱️ | Brendan's Content | 4.1 TB | ~220,000 | High | Apr 5, 2025 | Online Videos completion |
| ⏱️ | Media Platform | 2.2 TB | ~6,600 | Medium | Apr 10, 2025 | Dharma Talks completion |
| ⏱️ | Teachable Courses | 742 GB | ~1,800 | Medium | Apr 15, 2025 | None |

## User Onboarding Status

| Department | Users | Training | Setup Complete | Parallel Usage | Verification | Status |
|------------|-------|----------|----------------|----------------|--------------|--------|
| WebOps | 3 | ✅ | ✅ | ✅ | 🔄 | 🟨 In Progress |
| Online Programs | 5 | ✅ | ✅ | 🔄 | - | 🟨 In Progress |
| Communications | 4 | ✅ | ✅ | - | - | 🟨 In Progress |
| Administrative | 6 | ✅ | 🔄 | - | - | 🟨 In Progress |
| Teachers | 8 | 🔄 | - | - | - | 🟥 Not Started |
| Program | 5 | - | - | - | - | 🟥 Not Started |
| Outreach | 3 | - | - | - | - | 🟥 Not Started |
| Development | 4 | - | - | - | - | 🟥 Not Started |

## Infrastructure Status

| Component | Status | Details | Notes |
|-----------|--------|---------|-------|
| Wasabi Setup | 🟢 Complete | All buckets created and properly configured | Versioning enabled |
| NAS Configuration | 🟢 Complete | DS423 operational with all drives | 12TB used of 80TB capacity |
| AWS S3 Setup | 🟨 In Progress | Basic configuration complete | Lifecycle rules pending |
| Automation | 🟨 In Progress | Wasabi → NAS working | NAS → AWS pending |
| rclone Configuration | 🟢 Complete | All remotes configured | Migration script operational |
| Mountain Duck Distribution | 🟨 In Progress | 15/38 users configured | Standard bookmarks created |

## Performance Metrics

### Transfer Rates

| Connection Type | Average Speed | Peak Speed | Notes |
|----------------|---------------|------------|-------|
| Dropbox → NAS | 2 MiB/s | 15 MiB/s | Varies by file size and time of day |
| NAS → Wasabi | 25 MiB/s | 45 MiB/s | Limited by upload bandwidth |
| NAS → AWS | 20 MiB/s | 40 MiB/s | Limited by upload bandwidth |
| User → Wasabi | 5 MiB/s | 15 MiB/s | Via Mountain Duck |

### Time Estimates

| Transfer Size | Estimated Time | Notes |
|---------------|----------------|-------|
| < 1 GB | < 1 hour | Typically minutes |
| 1-100 GB | 1-12 hours | Dependent on file count |
| 100 GB - 1 TB | 12-48 hours | Large variations based on file size |
| > 1 TB | 2-7 days | Plan for weekends |

## Issue Tracking

### Active Issues

| ID | Issue | Impact | Status | Resolution Plan |
|----|-------|--------|--------|----------------|
| #023 | Dropbox API rate limiting | Medium | 🟨 In Progress | Implemented tpslimit parameter |
| #027 | Resource fork files failing verification | Low | 🟨 In Progress | Skip verification for these files |
| #031 | Mountain Duck connection drops | Medium | 🟨 In Progress | Testing new version |

### Resolved Issues

| ID | Issue | Impact | Resolution | Date Resolved |
|----|-------|--------|------------|---------------|
| #016 | NAS connection timeout | High | Increased timeout setting | Mar 15, 2025 |
| #018 | File permission errors | Medium | Updated SMB configuration | Mar 17, 2025 |
| #022 | Wasabi bucket configuration | Low | Enabled versioning | Mar 20, 2025 |

## Risk Assessment

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| Network interruption during transfer | Medium | Medium | Resume capability in rclone |
| User error deleting source files | Low | High | Read-only access during migration |
| Verification failures | Medium | Medium | Multiple verification methods |
| Cost overruns | Low | Medium | Regular monitoring of storage usage |
| Timeline slippage | Medium | Low | Prioritization of critical content |

## Next Steps

- [ ] Complete AWS Deep Glacier configuration (by Apr 1)
- [ ] Finalize backup automation procedures (by Apr 5)
- [ ] Complete remaining user training sessions (by Apr 15)
- [ ] Develop disaster recovery testing procedure (by Apr 20)
- [ ] Prepare Dropbox decommissioning plan (by May 1)

## Notes & Updates

**March 25, 2025**: Started migration of Online Videos collection. Initial transfer speed is good at ~15 MiB/s.

**March 23, 2025**: Completed development media migration with zero verification issues. Added to dashboard.

**March 22, 2025**: Updated batch transfer script with improved progress monitoring and error handling.

**March 20, 2025**: Implemented Wasabi bucket versioning for additional data protection.

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