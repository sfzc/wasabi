







# Media Files Online Backup 8-31-2020 Size Verification Commands

## Notes on Usage

1. For extremely large folders, additional timeout parameters are included (--timeout=120s)
2. All commands include rate limiting (--tpslimit=1) to avoid Dropbox API "too_many_requests" errors
3. Consider adding delays between checking very large folders (wait 2-3 minutes)
4. For folders with thousands of files, the process may take several minutes to complete
5. Output is saved to JSON files for easy comparison and future reference Rate Limited Commands (--tpslimit=1)
6. These commands include rate limiting to avoid Dropbox API "too_many_requests" errors.



---



## ✔ 15_04 Furyu Schroeder Portraits   (small)

### ✔ Source location
```bash
rclone size "dropbox-wasabi-migration:/Media Files Online Backup 8-31-2020/15_04 Furyu Schroeder Portraits" --json --tpslimit=1 > original_schroeder_size.json
```

### ✔ Staged location
```bash
rclone size "dropbox-wasabi-migration:/WASABI-MIGRATION/Media Files Online Backup 8-31-2020/15_04 Furyu Schroeder Portraits" --json --tpslimit=1 > staged_schroeder_size.json
```

### ✔ Compare
```bash
cat original_schroeder_size.json
cat staged_schroeder_size.json
```

### ✔ RESULTS (match)

```bash
cat original_schroeder_size.json
{"count":5,"bytes":43710564,"sizeless":0}

cat staged_schroeder_size.json
{"count":5,"bytes":43710564,"sizeless":0}
```



------



## ✔ 2020 Letterhead and Envelopes   (small)

### ✔ Source location
```bash
rclone size "dropbox-wasabi-migration:/Media Files Online Backup 8-31-2020/2020 Letterhead and Envelopes" --json --tpslimit=1 > original_letterhead_size.json
```

### ✔ Staged location
```bash
rclone size "dropbox-wasabi-migration:/WASABI-MIGRATION/Media Files Online Backup 8-31-2020/2020 Letterhead and Envelopes" --json --tpslimit=1 > staged_letterhead_size.json
```

### ✔ Compare (match)
```bash
cat original_letterhead_size.json
cat staged_letterhead_size.json
```

### ✔ RESULTS

```bash
cat original_letterhead_size.json
{"count":2,"bytes":3161702,"sizeless":0}

cat staged_letterhead_size.json
{"count":2,"bytes":3161702,"sizeless":0}
```



------



## ✔ Communication_media   (medium)

### ✔ Source location
```bash
rclone size "dropbox-wasabi-migration:/Media Files Online Backup 8-31-2020/Communication_media" --json --tpslimit=1 --timeout=120s > original_communication_media_size.json
```

### ✔ Staged location
```bash
rclone size "dropbox-wasabi-migration:/WASABI-MIGRATION/Media Files Online Backup 8-31-2020/Communication_media" --json --tpslimit=1 --timeout=120s > staged_communication_media_size.json
```

### ✔ Compare
```bash
cat original_communication_media_size.json
cat staged_communication_media_size.json
```

### ✔ RESULTS (matched)

```bash
❯ cat original_communication_media_size.json
{"count":2004,"bytes":656456173078,"sizeless":0}

❯ cat staged_communication_media_size.json
{"count":2004,"bytes":656456173078,"sizeless":0}

```



------



## ✔ Cut 9.0   (small)

### ✔ Source location
```bash
rclone size "dropbox-wasabi-migration:/Media Files Online Backup 8-31-2020/Cut 9.0" --json --tpslimit=1 > original_cut9_size.json
```

### ✔ Staged location
```bash
rclone size "dropbox-wasabi-migration:/WASABI-MIGRATION/Media Files Online Backup 8-31-2020/Cut 9.0" --json --tpslimit=1 > staged_cut9_size.json
```

### ✔ Compare
```bash
cat original_cut9_size.json
cat staged_cut9_size.json
```

### ✔ RESULTS (match)

```bash
cat original_cut9_size.json
{"count":83,"bytes":11094368063,"sizeless":0}

cat staged_cut9_size.json
{"count":83,"bytes":11094368063,"sizeless":0}✔ 
```



------



## ✔ development media   (large)

### ✔ Source location
```bash
rclone size "dropbox-wasabi-migration:/Media Files Online Backup 8-31-2020/development media" --json --tpslimit=1 > original_development_media_size.json
```

### ✔ Staged location
```bash
rclone size "dropbox-wasabi-migration:/WASABI-MIGRATION/Media Files Online Backup 8-31-2020/development media" --json --tpslimit=1 > staged_development_media_size.json
```

### ✔ Compare
```bash
cat original_development_media_size.json
cat staged_development_media_size.json
```

### ✔ RESULTS (matched)

```bash
cat original_development_media_size.json
{"count":5193,"bytes":1176748717583,"sizeless":0}

❯ cat staged_development_media_size.json
{"count":5193,"bytes":1176748717583,"sizeless":0}
```



------



## ✔ Digital Voice Editor   (small)

### ✔ Source location
```bash
rclone size "dropbox-wasabi-migration:/Media Files Online Backup 8-31-2020/Digital Voice Editor" --json --tpslimit=1 > original_digital_voice_size.json
```

### ✔ Staged location
```bash
rclone size "dropbox-wasabi-migration:/WASABI-MIGRATION/Media Files Online Backup 8-31-2020/Digital Voice Editor" --json --tpslimit=1 > staged_digital_voice_size.json
```

### ✔ Compare
```bash
cat original_digital_voice_size.json
cat staged_digital_voice_size.json
```

### ✔ RESULTS (match)

```bash
cat original_digital_voice_size.json
{"count":84,"bytes":49861050,"sizeless":0}

cat staged_digital_voice_size.json
{"count":84,"bytes":49861050,"sizeless":0}
```



---



## ✔ Experts_Mind_2010   (medium)

### ✔ Source location
```bash
rclone size "dropbox-wasabi-migration:/Media Files Online Backup 8-31-2020/Experts_Mind_2010" --json --tpslimit=1 > original_experts_mind_size.json
```

### ✔ Staged location
```bash
rclone size "dropbox-wasabi-migration:/WASABI-MIGRATION/Media Files Online Backup 8-31-2020/Experts_Mind_2010" --json --tpslimit=1 > staged_experts_mind_size.json
```

### ✔ Compare
```bash
cat original_experts_mind_size.json
cat staged_experts_mind_size.json
```

### ✔ RESULTS (match)

```bash
cat original_experts_mind_size.json
{"count":361,"bytes":5927290654,"sizeless":0}

cat staged_experts_mind_size.json
{"count":361,"bytes":5927290654,"sizeless":0}
```



---



## ✔ Fonts   (small)

### ✔ Source location
```bash
rclone size "dropbox-wasabi-migration:/Media Files Online Backup 8-31-2020/Fonts" --json --tpslimit=1 > original_fonts_size.json
```

### ✔ Staged location
```bash
rclone size "dropbox-wasabi-migration:/WASABI-MIGRATION/Media Files Online Backup 8-31-2020/Fonts" --json --tpslimit=1 > staged_fonts_size.json
```

### ✔ Compare
```bash
cat original_fonts_size.json
cat staged_fonts_size.json
```

### ✔ RESULTS (match)

```bash
cat original_fonts_size.json
{"count":758,"bytes":627886222,"sizeless":0}

cat staged_fonts_size.json
{"count":758,"bytes":627886222,"sizeless":0}✔ 
```



---



## ✔ Linda Oryoki Cut 3.0   (small)

### ✔ Source location
```bash
rclone size "dropbox-wasabi-migration:/Media Files Online Backup 8-31-2020/Linda Oryoki Cut 3.0" --json --tpslimit=1 > original_linda_oryoki_size.json
```

### ✔ Staged location
```bash
rclone size "dropbox-wasabi-migration:/WASABI-MIGRATION/Media Files Online Backup 8-31-2020/Linda Oryoki Cut 3.0" --json --tpslimit=1 > staged_linda_oryoki_size.json
```

### ✔ Compare
```bash
cat original_linda_oryoki_size.json
cat staged_linda_oryoki_size.json
```

### ✔ RESULTS (match)

```bash
cat original_linda_oryoki_size.json
{"count":1,"bytes":179940770,"sizeless":0}


cat staged_linda_oryoki_size.json
{"count":1,"bytes":179940770,"sizeless":0}
```



---



## Logos   (small)

### Source location
```bash
rclone size "dropbox-wasabi-migration:/Media Files Online Backup 8-31-2020/Logos" --json --tpslimit=1 > original_logos_size.json
```

### Staged location
```bash
rclone size "dropbox-wasabi-migration:/WASABI-MIGRATION/Media Files Online Backup 8-31-2020/Logos" --json --tpslimit=1 > staged_logos_size.json
```

### Compare
```bash
cat original_logos_size.json
cat staged_logos_size.json
```

### RESULTS

```bash
cat original_logos_size.json
{"count":93,"bytes":78692861,"sizeless":0}

cat staged_logos_size.json
{"count":93,"bytes":78692861,"sizeless":0}
```



---



## ✔ Mountain Seat Ceremonies   (large)

### ✔ Source location
```bash
rclone size "dropbox-wasabi-migration:/Media Files Online Backup 8-31-2020/Mountain Seat Ceremonies" --json --tpslimit=1 --timeout=120s > original_mountain_seat_size.json
```

### ✔ Staged location
```bash
rclone size "dropbox-wasabi-migration:/WASABI-MIGRATION/Media Files Online Backup 8-31-2020/Mountain Seat Ceremonies" --json --tpslimit=1 --timeout=120s > staged_mountain_seat_size.json
```

### ✔ Compare
```bash
cat original_mountain_seat_size.json
cat staged_mountain_seat_size.json
```

### ✔ RESULTS (match)

```bash
cat original_mountain_seat_size.json
{"count":16,"bytes":23336402803,"sizeless":0}

cat staged_mountain_seat_size.json
{"count":16,"bytes":23336402803,"sizeless":0}
```



---



## Multimedia drive   (large)

### ✔ Source location
```bash
rclone size "dropbox-wasabi-migration:/Media Files Online Backup 8-31-2020/Multimedia drive" --json --tpslimit=1 > original_multimedia_drive_size.json
```

### ✔ Staged location
```bash
rclone size "dropbox-wasabi-migration:/WASABI-MIGRATION/Media Files Online Backup 8-31-2020/Multimedia drive" --json --tpslimit=1 > staged_multimedia_drive_size.json
```

### ✔ Compare
```bash
cat original_multimedia_drive_size.json
cat staged_multimedia_drive_size.json
```

### ✔ RESULTS (matched)

```bash
cat original_multimedia_drive_size.json
{"count":13732,"bytes":160944055898,"sizeless":0}

❯ cat staged_multimedia_drive_size.json
{"count":13732,"bytes":160944055898,"sizeless":0}
```



---



## MYL2006 Digital Files   (small)

### Source location
```bash
rclone size "dropbox-wasabi-migration:/Media Files Online Backup 8-31-2020/MYL2006 Digital Files" --json --tpslimit=1 > original_myl2006_size.json
```

### Staged location
```bash
rclone size "dropbox-wasabi-migration:/WASABI-MIGRATION/Media Files Online Backup 8-31-2020/MYL2006 Digital Files" --json --tpslimit=1 > staged_myl2006_size.json
```

### Compare
```bash
cat original_myl2006_size.json
cat staged_myl2006_size.json
```

---





## Path of Urban Practice   (small)

### Source location
```bash
rclone size "dropbox-wasabi-migration:/Media Files Online Backup 8-31-2020/Path of Urban Practice" --json --tpslimit=1 > original_urban_practice_size.json
```

### Staged location
```bash
rclone size "dropbox-wasabi-migration:/WASABI-MIGRATION/Media Files Online Backup 8-31-2020/Path of Urban Practice" --json --tpslimit=1 > staged_urban_practice_size.json
```

### Compare
```bash
cat original_urban_practice_size.json
cat staged_urban_practice_size.json
```

---





## Paul Haller   (small)

### Source location
```bash
rclone size "dropbox-wasabi-migration:/Media Files Online Backup 8-31-2020/Paul Haller" --json --tpslimit=1 > original_paul_haller_size.json
```

### Staged location
```bash
rclone size "dropbox-wasabi-migration:/WASABI-MIGRATION/Media Files Online Backup 8-31-2020/Paul Haller" --json --tpslimit=1 > staged_paul_haller_size.json
```

### Compare
```bash
cat original_paul_haller_size.json
cat staged_paul_haller_size.json
```

---





## PHOTO ARCHIVES   (large)

### Source location
```bash
rclone size "dropbox-wasabi-migration:/Media Files Online Backup 8-31-2020/PHOTO ARCHIVES" --json --tpslimit=1 --timeout=120s > original_photo_archives_size.json

---
RESULT

rclone size "dropbox-wasabi-migration:/Media Files Online Backup 8-31-2020/PHOTO ARCHIVES" --json --tpslimit=1 --timeout=120s > original_photo_archives_size.json
2025/03/27 18:44:11 ERROR : Greens Restaurant for Katie: error listing: directory not found
2025/03/27 18:44:32 ERROR : Images for Catherine 11-2024: error listing: directory not found
2025/03/27 18:56:06 NOTICE: Failed to size with 3 errors: last error was: directory not found

```



### ✔ Staged location

```bash
rclone size "dropbox-wasabi-migration:/WASABI-MIGRATION/Media Files Online Backup 8-31-2020/PHOTO ARCHIVES" --json --tpslimit=1 --timeout=120s > staged_photo_archives_size.json
```

### Compare
```bash
cat original_photo_archives_size.json
✔ cat staged_photo_archives_size.json
```

### RESULTS

```bash
cat original_photo_archives_size.json
[FAILED]

cat staged_photo_archives_size.json
{"count":55521,"bytes":539369247692,"sizeless":0}
```



---



## Program Communications   (small)

### Source location
```bash
rclone size "dropbox-wasabi-migration:/Media Files Online Backup 8-31-2020/Program Communications" --json --tpslimit=1 --timeout=120s > original_program_communications_size.json
```

### Staged location
```bash
rclone size "dropbox-wasabi-migration:/WASABI-MIGRATION/Media Files Online Backup 8-31-2020/Program Communications" --json --tpslimit=1 --timeout=120s > staged_program_communications_size.json
```

### Compare
```bash
cat original_program_communications_size.json
cat staged_program_communications_size.json
```

### RESULTS

```bash

```



---



## Program Dept. Projects   (medium)

### Source location
```bash
rclone size "dropbox-wasabi-migration:/Media Files Online Backup 8-31-2020/Program Dept. Projects" --json --tpslimit=1 > original_program_dept_size.json
```

### Staged location
```bash
rclone size "dropbox-wasabi-migration:/WASABI-MIGRATION/Media Files Online Backup 8-31-2020/Program Dept. Projects" --json --tpslimit=1 > staged_program_dept_size.json
```

### Compare
```bash
cat original_program_dept_size.json
cat staged_program_dept_size.json
```

### RESULTS

```bash

```



---



## scan   (small)

### Source location
```bash
rclone size "dropbox-wasabi-migration:/Media Files Online Backup 8-31-2020/scan" --json --tpslimit=1 > original_scan_size.json
```

### Staged location
```bash
rclone size "dropbox-wasabi-migration:/WASABI-MIGRATION/Media Files Online Backup 8-31-2020/scan" --json --tpslimit=1 > staged_scan_size.json
```

### Compare
```bash
cat original_scan_size.json
cat staged_scan_size.json
```

### RESULTS

```bash

```



---



## Skit Night 2017   (small)

### Source location
```bash
rclone size "dropbox-wasabi-migration:/Media Files Online Backup 8-31-2020/Skit Night 2017" --json --tpslimit=1 > original_skit_night_size.json
```

### Staged location
```bash
rclone size "dropbox-wasabi-migration:/WASABI-MIGRATION/Media Files Online Backup 8-31-2020/Skit Night 2017" --json --tpslimit=1 > staged_skit_night_size.json
```

### Compare
```bash
cat original_skit_night_size.json
cat staged_skit_night_size.json
```

### RESULTS

```bash

```



---



## Style Manual   (small)

### Source location
```bash
rclone size "dropbox-wasabi-migration:/Media Files Online Backup 8-31-2020/Style Manual" --json --tpslimit=1 > original_style_manual_size.json
```

### Staged location
```bash
rclone size "dropbox-wasabi-migration:/WASABI-MIGRATION/Media Files Online Backup 8-31-2020/Style Manual" --json --tpslimit=1 > staged_style_manual_size.json
```

### Compare
```bash
cat original_style_manual_size.json
cat staged_style_manual_size.json
```

### RESULTS

```bash

```



---



## Taryn's Backup   (medium)

### Source location
```bash
rclone size "dropbox-wasabi-migration:/Media Files Online Backup 8-31-2020/Taryn's Backup" --json --tpslimit=1 > original_taryn_size.json
```

### Staged location
```bash
rclone size "dropbox-wasabi-migration:/WASABI-MIGRATION/Media Files Online Backup 8-31-2020/Taryn's Backup" --json --tpslimit=1 > staged_taryn_size.json
```

### Compare
```bash
cat original_taryn_size.json
cat staged_taryn_size.json
```

### RESULTS

```bash

```



---



## Test Folder - Don't touch   (small)

### Source location
```bash
rclone size "dropbox-wasabi-migration:/Media Files Online Backup 8-31-2020/Test Folder - Don't touch" --json --tpslimit=1 > original_test_folder_size.json
```

### Staged location
```bash
rclone size "dropbox-wasabi-migration:/WASABI-MIGRATION/Media Files Online Backup 8-31-2020/Test Folder - Don't touch" --json --tpslimit=1 > staged_test_folder_size.json
```

### Compare
```bash
cat original_test_folder_size.json
cat staged_test_folder_size.json
```

### RESULTS

```bash

```



---



## Videos, Tass Rez   (medium)

### Source location
```bash
rclone size "dropbox-wasabi-migration:/Media Files Online Backup 8-31-2020/Videos, Tass Rez" --json --tpslimit=1 > original_videos_tass_size.json
```

### Staged location
```bash
rclone size "dropbox-wasabi-migration:/WASABI-MIGRATION/Media Files Online Backup 8-31-2020/Videos, Tass Rez" --json --tpslimit=1 > staged_videos_tass_size.json
```

### Compare
```bash
cat original_videos_tass_size.json
cat staged_videos_tass_size.json
```

### RESULTS

```bash

```



---



## Volunteer Appreciation Nov 07 photos   (small)

### Source location
```bash
rclone size "dropbox-wasabi-migration:/Media Files Online Backup 8-31-2020/Volunteer Appreci...n Nov 07 photos" --json --tpslimit=1 > original_volunteer_size.json
```

### Staged location
```bash
rclone size "dropbox-wasabi-migration:/WASABI-MIGRATION/Media Files Online Backup 8-31-2020/Volunteer Appreci...n Nov 07 photos" --json --tpslimit=1 > staged_volunteer_size.json
```

### Compare
```bash
cat original_volunteer_size.json
cat staged_volunteer_size.json
```

### RESULTS

```bash

```



---



## Website Redesign - Barbara   (small)

### Source location
```bash
rclone size "dropbox-wasabi-migration:/Media Files Online Backup 8-31-2020/Website Redesign - Barbara" --json --tpslimit=1 > original_barbara_size.json
```



### Staged location

```bash
rclone size "dropbox-wasabi-migration:/WASABI-MIGRATION/Media Files Online Backup 8-31-2020/Website Redesign - Barbara" --json --tpslimit=1 > staged_barbara_size.json
```

### Compare
```bash
cat original_barbara_size.json
cat staged_barbara_size.json
```

### RESULTS

```bash

```



---



## Website Redesign - Earthlyn   (small)

### Source location
```bash
rclone size "dropbox-wasabi-migration:/Media Files Online Backup 8-31-2020/Website Redesign - Earthlyn" --json --tpslimit=1 > original_earthlyn_size.json
```

### Staged location
```bash
rclone size "dropbox-wasabi-migration:/WASABI-MIGRATION/Media Files Online Backup 8-31-2020/Website Redesign - Earthlyn" --json --tpslimit=1 > staged_earthlyn_size.json
```

### Compare
```bash
cat original_earthlyn_size.json
cat staged_earthlyn_size.json
```

### RESULTS

```bash

```



---



## Wendy Johnson interview   (small)

### Source location
```bash
rclone size "dropbox-wasabi-migration:/Media Files Online Backup 8-31-2020/Wendy Johnson interview" --json --tpslimit=1 > original_wendy_size.json
```

### Staged location
```bash
rclone size "dropbox-wasabi-migration:/WASABI-MIGRATION/Media Files Online Backup 8-31-2020/Wendy Johnson interview" --json --tpslimit=1 > staged_wendy_size.json
```

### Compare
```bash
cat original_wendy_size.json
cat staged_wendy_size.json
```

### RESULTS

```bash

```



---



## YEAR END LETTERS   (small)

### Source location
```bash
rclone size "dropbox-wasabi-migration:/Media Files Online Backup 8-31-2020/YEAR END LETTERS" --json --tpslimit=1 > original_year_end_size.json
```

### Staged location
```bash
rclone size "dropbox-wasabi-migration:/WASABI-MIGRATION/Media Files Online Backup 8-31-2020/YEAR END LETTERS" --json --tpslimit=1 > staged_year_end_size.json
```

### Compare
```bash
cat original_year_end_size.json
cat staged_year_end_size.json
```

### RESULTS

```bash

```



---



## ZMC Dharma Talks Fall 2016   (small)

### Source location
```bash
rclone size "dropbox-wasabi-migration:/Media Files Online Backup 8-31-2020/ZMC Dharma Talks Fall 2016" --json --tpslimit=1 > original_zmc_size.json
```

### Staged location
```bash
rclone size "dropbox-wasabi-migration:/WASABI-MIGRATION/Media Files Online Backup 8-31-2020/ZMC Dharma Talks Fall 2016" --json --tpslimit=1 > staged_zmc_size.json
```

### Compare
```bash
cat original_zmc_size.json
cat staged_zmc_size.json
```

### RESULTS

```bash

```





**END**
