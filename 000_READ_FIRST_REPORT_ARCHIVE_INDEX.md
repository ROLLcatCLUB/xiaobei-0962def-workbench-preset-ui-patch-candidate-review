# Xiaobei Report Archive Index 1.5.5

This file is the first-stop index for old audit reports, review packages, and future report placement.

清扫时间：2026-06-06

当前项目目录：

`D:\Documents\SmartEdu\xiaobei-core`

## Current Rule

后续新线产生的报告、复核包、ZIP、GPT review area 材料，默认不再长期落入当前项目目录。

推荐外部报告根目录：

`D:\Documents\SmartEdu\xiaobei-core-external-reports`

当前项目内只保留：

- 必要的源码、运行文件、轻量 contract/schema
- 当前正在执行阶段必须读取的小型输出
- 本索引文件和必要的追溯指针

不建议再长期放入项目内：

- 大型 ZIP
- 历史 audit package
- 旧 smoke 输出
- 下载教材资源包
- 旧阶段临时验证样本

## 1.5.5 Pre-Cleanup Backup

完整备份目录：

`D:\Documents\SmartEdu\xiaobei-core-backups\xiaobei-core_1.5.5_pre_cleanup_20260606_183757`

备份规模：

- 57,800 files
- 18.8 GB

用途：

- 找回清扫前完整项目状态
- 追溯任何被外移的旧报告、旧包、旧输出
- 必要时做人工恢复

## 1.5.5 Cleanout Archive

外移目录：

`D:\Documents\SmartEdu\xiaobei-core-cleanout-1.5.5\cleanup_20260606_184047`

外移规模：

- 47,186 files
- 18.26 GB

主要桶：

- `docs_audit`
- `docs_audit_packages`
- `docs_audit_legacy_contains_stage`
- `docs_audit_packages_legacy_contains_stage`
- `docs_audit_legacy_final_sweep`
- `outputs_legacy_except_current_lines`
- `top_level_low_risk`
- `root_legacy_loose_files`

清扫清单：

`D:\Documents\SmartEdu\xiaobei-core-cleanout-1.5.5\cleanup_20260606_184047\cleanup_manifest_1.5.5.json`

二次 audit 清扫清单：

`D:\Documents\SmartEdu\xiaobei-core-cleanout-1.5.5\cleanup_20260606_184047\cleanup_manifest_1.5.5_second_pass_audit.json`

最终 audit 清扫清单：

`D:\Documents\SmartEdu\xiaobei-core-cleanout-1.5.5\cleanup_20260606_184047\cleanup_manifest_1.5.5_final_audit_sweep.json`

源码类二次清扫候选清单：

`D:\Documents\SmartEdu\xiaobei-core-cleanout-1.5.5\cleanup_20260606_184047\manual_review_code_candidates_1.5.5.json`

## How To Trace Old Reports

先查当前项目：

```powershell
rg -n "0955F|0954P|target stage id" D:\Documents\SmartEdu\xiaobei-core
```

如果当前项目查不到，查 cleanout：

```powershell
rg -n "0955F|0954P|target stage id" D:\Documents\SmartEdu\xiaobei-core-cleanout-1.5.5\cleanup_20260606_184047
```

如果 cleanout 仍查不到，查完整备份：

```powershell
rg -n "0955F|0954P|target stage id" D:\Documents\SmartEdu\xiaobei-core-backups\xiaobei-core_1.5.5_pre_cleanup_20260606_183757
```

## New Line Start Checklist

1. Read this file first.
2. Check current project `docs/foundation` for active contracts and schemas.
3. Check external reports root for recent report packages.
4. If older evidence is needed, search the cleanout archive.
5. If full pre-cleanup state is needed, search the 1.5.5 backup.

## Future Report Placement

For a new stage, use an external folder like:

`D:\Documents\SmartEdu\xiaobei-core-external-reports\0956A_STAGE_NAME_YYYYMMDD_HHMMSS`

Inside that folder, put:

- report markdown/json
- checklist/result
- review ZIP
- manifest
- GPT handoff materials

If the project itself needs a pointer, add only a small index entry or lightweight contract. Do not reintroduce large historical report bundles into the project root.

## Current External Report Pointers

### 0956A Field Scheme Permission Scope Contract

外部报告目录：

`D:\Documents\SmartEdu\xiaobei-core-external-reports\0956A_FIELD_SCHEME_PERMISSION_SCOPE_CONTRACT_20260606_192050`

项目内轻量产物：

- `docs/foundation/field_scheme_permission_scope_contract_0956A.md`
- `docs/foundation/field_scheme_permission_scope_contract_0956A.json`
- `scripts/validate_field_scheme_permission_scope_contract_0956A.py`

外部审核包：

`D:\Documents\SmartEdu\xiaobei-core-external-reports\0956A_FIELD_SCHEME_PERMISSION_SCOPE_CONTRACT_20260606_192050\0956A_field_scheme_permission_scope_contract_review_package.zip`

状态：

```text
0956A_FIELD_SCHEME_PERMISSION_SCOPE_CONTRACT=PASS
NEXT_STAGE=0956B_FIELD_SCHEME_SCHEMA_CONTRACT
NEXT_STAGE_REQUIRES_EXPLICIT_DECISION=false
```

### 0956B Field Scheme Schema Contract

外部报告目录：

`D:\Documents\SmartEdu\xiaobei-core-external-reports\0956B_FIELD_SCHEME_SCHEMA_CONTRACT_20260606_193601`

项目内轻量产物：

- `docs/foundation/field_scheme_schema_contract_0956B.md`
- `docs/foundation/field_scheme_schema_contract_0956B.json`
- `docs/foundation/field_scheme_schema_0956B.json`
- `scripts/validate_field_scheme_schema_contract_0956B.py`

外部审核包：

`D:\Documents\SmartEdu\xiaobei-core-external-reports\0956B_FIELD_SCHEME_SCHEMA_CONTRACT_20260606_193601\0956B_field_scheme_schema_contract_review_package.zip`

状态：

```text
0956B_FIELD_SCHEME_SCHEMA_CONTRACT=PASS
NEXT_STAGE=0956C_ART_FIELD_SCHEME_DEFAULT_FIXTURE_CONTRACT
NEXT_STAGE_REQUIRES_EXPLICIT_DECISION=false
```

### 0956C Art Field Scheme Default Fixture Contract

外部报告目录：

`D:\Documents\SmartEdu\xiaobei-core-external-reports\0956C_ART_FIELD_SCHEME_DEFAULT_FIXTURE_CONTRACT_20260606_194726`

项目内轻量产物：

- `docs/foundation/art_field_scheme_default_fixture_contract_0956C.md`
- `docs/foundation/art_field_scheme_default_fixture_contract_0956C.json`
- `samples/field_scheme_0956C/art_unit_brief_default_fixture_0956C.json`
- `scripts/validate_art_field_scheme_default_fixture_contract_0956C.py`

外部审核包：

`D:\Documents\SmartEdu\xiaobei-core-external-reports\0956C_ART_FIELD_SCHEME_DEFAULT_FIXTURE_CONTRACT_20260606_194726\0956C_art_field_scheme_default_fixture_contract_review_package.zip`

状态：

```text
0956C_ART_FIELD_SCHEME_DEFAULT_FIXTURE_CONTRACT=PASS
NEXT_STAGE=0956D_ART_FIELD_SCHEME_DEFAULT_FIXTURE_SMOKE
NEXT_STAGE_REQUIRES_EXPLICIT_DECISION=false
```

### 0956D Art Field Scheme Default Fixture Smoke

外部报告目录：

`D:\Documents\SmartEdu\xiaobei-core-external-reports\0956D_ART_FIELD_SCHEME_DEFAULT_FIXTURE_SMOKE_20260606_204932`

项目内轻量产物：

- `docs/foundation/art_field_scheme_default_fixture_smoke_0956D.md`
- `docs/foundation/art_field_scheme_default_fixture_smoke_0956D.json`
- `scripts/validate_art_field_scheme_default_fixture_smoke_0956D.py`

外部审核包：

`D:\Documents\SmartEdu\xiaobei-core-external-reports\0956D_ART_FIELD_SCHEME_DEFAULT_FIXTURE_SMOKE_20260606_204932\0956D_art_field_scheme_default_fixture_smoke_review_package.zip`

状态：

```text
0956D_ART_FIELD_SCHEME_DEFAULT_FIXTURE_SMOKE=PASS
NEXT_STAGE=0956E_FIELD_SCHEME_REVIEW_WORKSPACE_CONTRACT
NEXT_STAGE_REQUIRES_EXPLICIT_DECISION=false
```

### 0956E Field Scheme Review Workspace Contract

外部报告目录：

`D:\Documents\SmartEdu\xiaobei-core-external-reports\0956E_FIELD_SCHEME_REVIEW_WORKSPACE_CONTRACT_20260606_205623`

项目内轻量产物：

- `docs/foundation/field_scheme_review_workspace_contract_0956E.md`
- `docs/foundation/field_scheme_review_workspace_contract_0956E.json`
- `docs/foundation/field_scheme_review_workspace_viewmodel_schema_0956E.json`
- `scripts/validate_field_scheme_review_workspace_contract_0956E.py`

外部审核包：

`D:\Documents\SmartEdu\xiaobei-core-external-reports\0956E_FIELD_SCHEME_REVIEW_WORKSPACE_CONTRACT_20260606_205623\0956E_field_scheme_review_workspace_contract_review_package.zip`

状态：

```text
0956E_FIELD_SCHEME_REVIEW_WORKSPACE_CONTRACT=PASS
NEXT_STAGE=0956F_FIELD_SCHEME_REVIEW_WORKSPACE_READONLY_PREVIEW_APPLY
NEXT_STAGE_REQUIRES_EXPLICIT_DECISION=false
```

### 0956F Field Scheme Review Workspace Readonly Preview Apply

外部报告目录：

`D:\Documents\SmartEdu\xiaobei-core-external-reports\0956F_FIELD_SCHEME_REVIEW_WORKSPACE_READONLY_PREVIEW_APPLY_20260606_211353`

项目内轻量产物：

- `docs/foundation/field_scheme_review_workspace_readonly_preview_apply_0956F.md`
- `docs/foundation/field_scheme_review_workspace_readonly_preview_apply_0956F.json`
- `outputs/field_scheme_0956F/review_workspace_preview_0956F.json`
- `scripts/validate_field_scheme_review_workspace_readonly_preview_apply_0956F.py`

外部审核包：

`D:\Documents\SmartEdu\xiaobei-core-external-reports\0956F_FIELD_SCHEME_REVIEW_WORKSPACE_READONLY_PREVIEW_APPLY_20260606_211353\0956F_field_scheme_review_workspace_readonly_preview_apply_review_package.zip`

状态：

```text
0956F_FIELD_SCHEME_REVIEW_WORKSPACE_READONLY_PREVIEW_APPLY=PASS
NEXT_STAGE=0956G_FIELD_SCHEME_PATCH_CANDIDATE_READONLY_APPLY
NEXT_STAGE_REQUIRES_EXPLICIT_DECISION=false
```

### 0956G Field Scheme Patch Candidate Readonly Apply

外部报告目录：

`D:\Documents\SmartEdu\xiaobei-core-external-reports\0956G_FIELD_SCHEME_PATCH_CANDIDATE_READONLY_APPLY_20260606_213916`

项目内轻量产物：

- `docs/foundation/field_scheme_patch_candidate_readonly_apply_0956G.md`
- `docs/foundation/field_scheme_patch_candidate_readonly_apply_0956G.json`
- `outputs/field_scheme_0956G/field_scheme_patch_candidates_0956G.json`
- `scripts/validate_field_scheme_patch_candidate_readonly_apply_0956G.py`

外部审核包：

`D:\Documents\SmartEdu\xiaobei-core-external-reports\0956G_FIELD_SCHEME_PATCH_CANDIDATE_READONLY_APPLY_20260606_213916\0956G_field_scheme_patch_candidate_readonly_apply_review_package.zip`

状态：

```text
0956G_FIELD_SCHEME_PATCH_CANDIDATE_READONLY_APPLY=PASS
PATCH_CANDIDATE_COUNT=4
PATCH_CANDIDATES_APPLIED=false
ACTIVE_FIELD_SCHEME_CREATED=false
FIELD_SCHEME_STORE_WRITTEN=false
NEXT_STAGE=0956H_FIELD_SCHEME_PATCH_CANDIDATE_PERMISSION_SMOKE
NEXT_STAGE_REQUIRES_EXPLICIT_DECISION=false
```

### 0956H Field Scheme Patch Candidate Permission Smoke

外部报告目录：

`D:\Documents\SmartEdu\xiaobei-core-external-reports\0956H_FIELD_SCHEME_PATCH_CANDIDATE_PERMISSION_SMOKE_20260606_221430`

项目内轻量产物：

- `docs/foundation/field_scheme_patch_candidate_permission_smoke_0956H.md`
- `docs/foundation/field_scheme_patch_candidate_permission_smoke_0956H.json`
- `outputs/field_scheme_0956H/patch_candidate_permission_smoke_0956H.json`
- `scripts/validate_field_scheme_patch_candidate_permission_smoke_0956H.py`

外部审核包：

`D:\Documents\SmartEdu\xiaobei-core-external-reports\0956H_FIELD_SCHEME_PATCH_CANDIDATE_PERMISSION_SMOKE_20260606_221430\0956H_field_scheme_patch_candidate_permission_smoke_review_package.zip`

状态：

```text
0956H_FIELD_SCHEME_PATCH_CANDIDATE_PERMISSION_SMOKE=PASS
SOURCE_PATCH_CANDIDATE_COUNT=4
BEGINNER_USER_SUBMIT_ALLOWED=false
INTERMEDIATE_USER_SUBMIT_ALLOWED=false
ADVANCED_USER_SUBMIT_ALLOWED=true
ADVANCED_USER_PUBLISH_ALLOWED=false
ADMINISTRATOR_PUBLISH_ALLOWED_NOW=false
ADMINISTRATOR_PUBLISH_REQUIRES_FUTURE_GATE=true
PATCH_CANDIDATES_APPLIED=false
ACTIVE_FIELD_SCHEME_CREATED=false
FIELD_SCHEME_STORE_WRITTEN=false
NEXT_STAGE=0956I_FIELD_SCHEME_PATCH_CANDIDATE_REVIEW_DECISION_CONTRACT
NEXT_STAGE_REQUIRES_EXPLICIT_DECISION=false
```

### 0956I Field Scheme Patch Candidate Review Decision Contract

外部报告目录：

`D:\Documents\SmartEdu\xiaobei-core-external-reports\0956I_FIELD_SCHEME_PATCH_CANDIDATE_REVIEW_DECISION_CONTRACT_20260606_223655`

项目内轻量产物：

- `docs/foundation/field_scheme_patch_candidate_review_decision_contract_0956I.md`
- `docs/foundation/field_scheme_patch_candidate_review_decision_contract_0956I.json`
- `docs/foundation/field_scheme_patch_candidate_review_decision_schema_0956I.json`
- `scripts/validate_field_scheme_patch_candidate_review_decision_contract_0956I.py`

外部审核包：

`D:\Documents\SmartEdu\xiaobei-core-external-reports\0956I_FIELD_SCHEME_PATCH_CANDIDATE_REVIEW_DECISION_CONTRACT_20260606_223655\0956I_field_scheme_patch_candidate_review_decision_contract_review_package.zip`

状态：

```text
0956I_FIELD_SCHEME_PATCH_CANDIDATE_REVIEW_DECISION_CONTRACT=PASS
ALLOWED_DECISION_TYPES=5
STATE_TRANSITION_COUNT=5
REVIEW_DECISION_CREATED=false
CANDIDATE_STATUS_CHANGED=false
PATCH_CANDIDATES_APPLIED=false
ACTIVE_FIELD_SCHEME_CREATED=false
FIELD_SCHEME_STORE_WRITTEN=false
ADMINISTRATOR_PUBLISH_REQUIRES_FUTURE_GATE=true
NEXT_STAGE=0956J_FIELD_SCHEME_REVIEW_DECISION_READONLY_PREVIEW_APPLY
NEXT_STAGE_REQUIRES_EXPLICIT_DECISION=false
```

### 0956J Field Scheme Review Decision Readonly Preview Apply

外部报告目录：

`D:\Documents\SmartEdu\xiaobei-core-external-reports\0956J_FIELD_SCHEME_REVIEW_DECISION_READONLY_PREVIEW_APPLY_20260606_225200`

项目内轻量产物：

- `docs/foundation/field_scheme_review_decision_readonly_preview_apply_0956J.md`
- `docs/foundation/field_scheme_review_decision_readonly_preview_apply_0956J.json`
- `outputs/field_scheme_0956J/review_decision_preview_0956J.json`
- `scripts/validate_field_scheme_review_decision_readonly_preview_apply_0956J.py`

外部审核包：

`D:\Documents\SmartEdu\xiaobei-core-external-reports\0956J_FIELD_SCHEME_REVIEW_DECISION_READONLY_PREVIEW_APPLY_20260606_225200\0956J_field_scheme_review_decision_readonly_preview_apply_review_package.zip`

状态：

```text
0956J_FIELD_SCHEME_REVIEW_DECISION_READONLY_PREVIEW_APPLY=PASS
PREVIEW_DECISION_COUNT=5
REAL_REVIEW_DECISION_CREATED=false
CANDIDATE_STATUS_CHANGED=false
PATCH_CANDIDATES_APPLIED=false
ACTIVE_FIELD_SCHEME_CREATED=false
FIELD_SCHEME_STORE_WRITTEN=false
NEXT_STAGE=0956K_FIELD_SCHEME_REVIEW_DECISION_READONLY_PREVIEW_SMOKE
NEXT_STAGE_REQUIRES_EXPLICIT_DECISION=false
```

### 0956K Field Scheme Review Decision Readonly Preview Smoke

外部报告目录：

`D:\Documents\SmartEdu\xiaobei-core-external-reports\0956K_FIELD_SCHEME_REVIEW_DECISION_READONLY_PREVIEW_SMOKE_20260606_220924`

项目内轻量产物：

- `docs/foundation/field_scheme_review_decision_readonly_preview_smoke_0956K.md`
- `docs/foundation/field_scheme_review_decision_readonly_preview_smoke_0956K.json`
- `outputs/field_scheme_0956K/review_decision_preview_smoke_0956K.json`
- `scripts/validate_field_scheme_review_decision_readonly_preview_smoke_0956K.py`

外部审核包：

`D:\Documents\SmartEdu\xiaobei-core-external-reports\0956K_FIELD_SCHEME_REVIEW_DECISION_READONLY_PREVIEW_SMOKE_20260606_220924\0956K_field_scheme_review_decision_readonly_preview_smoke_review_package.zip`

状态：

```text
0956K_FIELD_SCHEME_REVIEW_DECISION_READONLY_PREVIEW_SMOKE=PASS
PREVIEW_DECISION_COUNT=5
REAL_REVIEW_DECISIONS_EMPTY=true
ALL_DECISION_EFFECT_PREVIEW_ONLY=true
CANDIDATE_STATUS_CHANGED=false
PATCH_CANDIDATES_APPLIED=false
ACTIVE_FIELD_SCHEME_CREATED=false
FIELD_SCHEME_STORE_WRITTEN=false
NEXT_STAGE=0956L_FIELD_SCHEME_PATCH_CANDIDATE_PREVIEW_SEAL
NEXT_STAGE_REQUIRES_EXPLICIT_DECISION=false
```

### 0956L Field Scheme Patch Candidate Preview Seal

外部报告目录：

`D:\Documents\SmartEdu\xiaobei-core-external-reports\0956L_FIELD_SCHEME_PATCH_CANDIDATE_PREVIEW_SEAL_20260607_042656`

项目内轻量产物：

- `docs/foundation/field_scheme_patch_candidate_preview_seal_0956L.md`
- `docs/foundation/field_scheme_patch_candidate_preview_seal_0956L.json`
- `scripts/validate_field_scheme_patch_candidate_preview_seal_0956L.py`

外部审核包：

`D:\Documents\SmartEdu\xiaobei-core-external-reports\0956L_FIELD_SCHEME_PATCH_CANDIDATE_PREVIEW_SEAL_20260607_042656\0956L_field_scheme_patch_candidate_preview_seal_review_package.zip`

状态：

```text
0956L_FIELD_SCHEME_PATCH_CANDIDATE_PREVIEW_SEAL=SEALED
PATCH_CANDIDATE_COUNT=4
PREVIEW_DECISION_COUNT=5
REAL_REVIEW_DECISION_CREATED=false
CANDIDATE_STATUS_CHANGED=false
PATCH_CANDIDATES_APPLIED=false
ACTIVE_FIELD_SCHEME_CREATED=false
FIELD_SCHEME_STORE_WRITTEN=false
NEXT_STAGE=0956M_FIELD_SCHEME_REGISTRY_SCOPE_CONTRACT
NEXT_STAGE_REQUIRES_EXPLICIT_DECISION=false
```

### 0956M Field Scheme Registry Scope Contract

外部报告目录：

`D:\Documents\SmartEdu\xiaobei-core-external-reports\0956M_FIELD_SCHEME_REGISTRY_SCOPE_CONTRACT_20260607_043447`

项目内轻量产物：

- `docs/foundation/field_scheme_registry_scope_contract_0956M.md`
- `docs/foundation/field_scheme_registry_scope_contract_0956M.json`
- `scripts/validate_field_scheme_registry_scope_contract_0956M.py`

外部审核包：

`D:\Documents\SmartEdu\xiaobei-core-external-reports\0956M_FIELD_SCHEME_REGISTRY_SCOPE_CONTRACT_20260607_043447\0956M_field_scheme_registry_scope_contract_review_package.zip`

状态：

```text
0956M_FIELD_SCHEME_REGISTRY_SCOPE_CONTRACT=PASS
REGISTRY_SCOPE_DEFINED=true
REQUIRED_REGISTRY_ENTRY_FIELDS=22
REGISTRY_FILE_CREATED=false
REGISTRY_ENTRY_CREATED=false
REGISTRY_STORE_WRITTEN=false
REGISTRY_ROUTE_CREATED=false
ACTIVE_FIELD_SCHEME_CREATED=false
PROVIDER_CONTEXT_INJECTION=false
NEXT_STAGE=0956N_FIELD_SCHEME_REGISTRY_SCHEMA_CONTRACT
NEXT_STAGE_REQUIRES_EXPLICIT_DECISION=false
```

### 0956N Field Scheme Registry Schema Contract

外部报告目录：

`D:\Documents\SmartEdu\xiaobei-core-external-reports\0956N_FIELD_SCHEME_REGISTRY_SCHEMA_CONTRACT_20260607_044018`

项目内轻量产物：

- `docs/foundation/field_scheme_registry_schema_contract_0956N.md`
- `docs/foundation/field_scheme_registry_schema_contract_0956N.json`
- `docs/foundation/field_scheme_registry_entry_schema_0956N.json`
- `scripts/validate_field_scheme_registry_schema_contract_0956N.py`

外部审核包：

`D:\Documents\SmartEdu\xiaobei-core-external-reports\0956N_FIELD_SCHEME_REGISTRY_SCHEMA_CONTRACT_20260607_044018\0956N_field_scheme_registry_schema_contract_review_package.zip`

状态：

```text
0956N_FIELD_SCHEME_REGISTRY_SCHEMA_CONTRACT=PASS
REGISTRY_SCHEMA_DEFINED=true
SCHEMA_ID=field_scheme_registry_entry_schema_0956N
REQUIRED_REGISTRY_ENTRY_FIELDS=22
SCHEMA_REQUIRED_FIELDS=23
REGISTRY_FILE_CREATED=false
REGISTRY_ENTRY_CREATED=false
REGISTRY_STORE_WRITTEN=false
REGISTRY_ROUTE_CREATED=false
ACTIVE_FIELD_SCHEME_CREATED=false
NEXT_STAGE=0956O_FIELD_SCHEME_REGISTRY_SCHEMA_SMOKE
NEXT_STAGE_REQUIRES_EXPLICIT_DECISION=false
```

### 0956O Field Scheme Registry Schema Smoke

外部报告目录：

`D:\Documents\SmartEdu\xiaobei-core-external-reports\0956O_FIELD_SCHEME_REGISTRY_SCHEMA_SMOKE_20260607_044840`

项目内轻量产物：

- `docs/foundation/field_scheme_registry_schema_smoke_0956O.md`
- `docs/foundation/field_scheme_registry_schema_smoke_0956O.json`
- `samples/field_scheme_registry_0956O/legal_synthetic_registry_entry_0956O.json`
- `samples/field_scheme_registry_0956O/invalid_active_write_provider_registry_entry_0956O.json`
- `outputs/field_scheme_0956O/field_scheme_registry_schema_smoke_0956O.json`
- `scripts/validate_field_scheme_registry_schema_smoke_0956O.py`

外部审核包：

`D:\Documents\SmartEdu\xiaobei-core-external-reports\0956O_FIELD_SCHEME_REGISTRY_SCHEMA_SMOKE_20260607_044840\0956O_field_scheme_registry_schema_smoke_review_package.zip`

状态：

```text
0956O_FIELD_SCHEME_REGISTRY_SCHEMA_SMOKE=PASS
LEGAL_FIXTURE_PASS=true
INVALID_FIXTURE_REJECT=true
REGISTRY_FILE_CREATED=false
REGISTRY_ENTRY_CREATED=false
REGISTRY_STORE_WRITTEN=false
REGISTRY_ROUTE_CREATED=false
WORKBENCH_UI_BOUND=false
PROVIDER_CALLED=false
NEXT_STAGE=0956P_FIELD_SCHEME_REGISTRY_READONLY_ENTRY_PREVIEW_APPLY
NEXT_STAGE_REQUIRES_EXPLICIT_DECISION=false
```

### 0956P Field Scheme Registry Readonly Entry Preview Apply

外部报告目录：

`D:\Documents\SmartEdu\xiaobei-core-external-reports\0956P_FIELD_SCHEME_REGISTRY_READONLY_ENTRY_PREVIEW_APPLY_20260607_045652`

项目内轻量产物：

- `docs/foundation/field_scheme_registry_readonly_entry_preview_apply_0956P.md`
- `docs/foundation/field_scheme_registry_readonly_entry_preview_apply_0956P.json`
- `outputs/field_scheme_0956P/readonly_registry_entry_preview_0956P.json`
- `scripts/validate_field_scheme_registry_readonly_entry_preview_apply_0956P.py`

外部审核包：

`D:\Documents\SmartEdu\xiaobei-core-external-reports\0956P_FIELD_SCHEME_REGISTRY_READONLY_ENTRY_PREVIEW_APPLY_20260607_045652\0956P_field_scheme_registry_readonly_entry_preview_apply_review_package.zip`

状态：

```text
0956P_FIELD_SCHEME_REGISTRY_READONLY_ENTRY_PREVIEW_APPLY=PASS
PREVIEW_ENTRY_COUNT=1
REAL_REGISTRY_ENTRIES=[]
REGISTRY_FILE_CREATED=false
REGISTRY_ENTRY_CREATED=false
REGISTRY_STORE_WRITTEN=false
REGISTRY_ROUTE_CREATED=false
WORKBENCH_UI_BOUND=false
PROVIDER_CALLED=false
NEXT_STAGE=0956Q_FIELD_SCHEME_REGISTRY_READONLY_ENTRY_PREVIEW_SMOKE
NEXT_STAGE_REQUIRES_EXPLICIT_DECISION=false
```

### 0956Q Field Scheme Registry Readonly Entry Preview Smoke

外部报告目录：

`D:\Documents\SmartEdu\xiaobei-core-external-reports\0956Q_FIELD_SCHEME_REGISTRY_READONLY_ENTRY_PREVIEW_SMOKE_20260607_050417`

项目内轻量产物：

- `docs/foundation/field_scheme_registry_readonly_entry_preview_smoke_0956Q.md`
- `docs/foundation/field_scheme_registry_readonly_entry_preview_smoke_0956Q.json`
- `outputs/field_scheme_0956Q/readonly_registry_entry_preview_smoke_0956Q.json`
- `scripts/validate_field_scheme_registry_readonly_entry_preview_smoke_0956Q.py`

外部审核包：

`D:\Documents\SmartEdu\xiaobei-core-external-reports\0956Q_FIELD_SCHEME_REGISTRY_READONLY_ENTRY_PREVIEW_SMOKE_20260607_050417\0956Q_field_scheme_registry_readonly_entry_preview_smoke_review_package.zip`

状态：

```text
0956Q_FIELD_SCHEME_REGISTRY_READONLY_ENTRY_PREVIEW_SMOKE=PASS
PREVIEW_ENTRY_COUNT=1
REAL_REGISTRY_ENTRIES=[]
PREVIEW_ONLY=true
REGISTRY_FILE_CREATED=false
REGISTRY_ENTRY_CREATED=false
REGISTRY_STORE_WRITTEN=false
REGISTRY_ROUTE_CREATED=false
WORKBENCH_UI_BOUND=false
PROVIDER_CALLED=false
ZIP_ENTRY_COUNT=10
SHA256=1cbe365ff12f1480b0b7586c55eaeab97c3b0aadf65f3e7af42a15db226f2b3c
NEXT_STAGE=0956R_FIELD_SCHEME_REGISTRY_PREVIEW_SEAL
NEXT_STAGE_REQUIRES_EXPLICIT_DECISION=false
```

### 0956R Field Scheme Registry Preview Seal

外部报告目录：

`D:\Documents\SmartEdu\xiaobei-core-external-reports\0956R_FIELD_SCHEME_REGISTRY_PREVIEW_SEAL_20260607_051027`

项目内轻量产物：

- `docs/foundation/field_scheme_registry_preview_seal_0956R.md`
- `docs/foundation/field_scheme_registry_preview_seal_0956R.json`
- `scripts/validate_field_scheme_registry_preview_seal_0956R.py`

外部审核包：

`D:\Documents\SmartEdu\xiaobei-core-external-reports\0956R_FIELD_SCHEME_REGISTRY_PREVIEW_SEAL_20260607_051027\0956R_field_scheme_registry_preview_seal_review_package.zip`

状态：

```text
0956R_FIELD_SCHEME_REGISTRY_PREVIEW_SEAL=SEALED
SEALED_STAGES=0956M,0956N,0956O,0956P,0956Q
REGISTRY_SCOPE_DEFINED=true
REGISTRY_SCHEMA_DEFINED=true
LEGAL_FIXTURE_PASS=true
INVALID_FIXTURE_REJECT=true
READONLY_REGISTRY_ENTRY_PREVIEW_CREATED=true
PREVIEW_ENTRY_COUNT=1
REAL_REGISTRY_ENTRIES=[]
REGISTRY_FILE_CREATED=false
REGISTRY_ENTRY_CREATED=false
REGISTRY_STORE_WRITTEN=false
REGISTRY_ROUTE_CREATED=false
WORKBENCH_UI_BOUND=false
PROVIDER_CALLED=false
ZIP_ENTRY_COUNT=15
SHA256=068e74d4178c2bfe113590e21dd1c299a71148a38f5ab7477db9e4ef0b6e765c
NEXT_STAGE=0956S_FIELD_SCHEME_OPEN_DEFINITION_LINE_V0_SEAL
NEXT_STAGE_REQUIRES_EXPLICIT_DECISION=false
```

### 0956S Field Scheme Open Definition Line V0 Seal

外部报告目录：

`D:\Documents\SmartEdu\xiaobei-core-external-reports\0956S_FIELD_SCHEME_OPEN_DEFINITION_LINE_V0_SEAL_20260607_051634`

项目内轻量产物：

- `docs/foundation/field_scheme_open_definition_line_v0_seal_0956S.md`
- `docs/foundation/field_scheme_open_definition_line_v0_seal_0956S.json`
- `scripts/validate_field_scheme_open_definition_line_v0_seal_0956S.py`

外部审核包：

`D:\Documents\SmartEdu\xiaobei-core-external-reports\0956S_FIELD_SCHEME_OPEN_DEFINITION_LINE_V0_SEAL_20260607_051634\0956S_field_scheme_open_definition_line_v0_seal_review_package.zip`

状态：

```text
0956S_FIELD_SCHEME_OPEN_DEFINITION_LINE_V0_SEAL=SEALED
SEALED_STAGE_COUNT=18
V0_CAPABILITY=contract_schema_fixture_preview_seal_only
PATCH_CANDIDATE_COUNT=4
REVIEW_DECISION_PREVIEW_COUNT=5
REGISTRY_PREVIEW_ENTRY_COUNT=1
REAL_REGISTRY_CREATED=false
REAL_REGISTRY_ENTRIES=[]
ACTIVE_FIELD_SCHEME_CREATED=false
FIELD_SCHEME_STORE_WRITTEN=false
REGISTRY_STORE_WRITTEN=false
WORKBENCH_UI_BOUND=false
PROVIDER_CALLED=false
NEXT_STAGE_REQUIRES_EXPLICIT_DECISION=true
ZIP_ENTRY_COUNT=13
SHA256=bbea909b0d8ec6f8aea19fc9188b2453b3c0dcba958211e9d05ac8fbba47bfea
NEXT_STAGE=0957A_FIELD_SCHEME_ACTIVATION_GATE_SCOPE_CONTRACT
```

### 0957A Field Scheme Activation Gate Scope Contract

外部报告目录：

`D:\Documents\SmartEdu\xiaobei-core-external-reports\0957A_FIELD_SCHEME_ACTIVATION_GATE_SCOPE_CONTRACT_20260607_053209`

项目内轻量产物：

- `docs/foundation/field_scheme_activation_gate_scope_contract_0957A.md`
- `docs/foundation/field_scheme_activation_gate_scope_contract_0957A.json`
- `scripts/validate_field_scheme_activation_gate_scope_contract_0957A.py`

外部审核包：

`D:\Documents\SmartEdu\xiaobei-core-external-reports\0957A_FIELD_SCHEME_ACTIVATION_GATE_SCOPE_CONTRACT_20260607_053209\0957A_field_scheme_activation_gate_scope_contract_review_package.zip`

状态：

```text
0957A_FIELD_SCHEME_ACTIVATION_GATE_SCOPE_CONTRACT=CONTRACT_PASS
PREVIOUS_STATUS=SEALED_WITH_PACKAGING_CAVEAT
ACTIVATION_GATE_DEFINED=true
ACTIVATION_GATE_PERFORMED=false
ORDINARY_TEACHER_VISIBLE_CHOICES=use_default_scheme,use_my_scheme,let_xiaobei_recommend
ORDINARY_TEACHER_INTERNAL_REGISTRY_STATES_HIDDEN=true
AGENT_DIRECT_ACTIVATION_ALLOWED=false
ACTIVE_FIELD_SCHEME_CREATED=false
REAL_REGISTRY_ENTRY_CREATED=false
REGISTRY_STORE_WRITTEN=false
FIELD_SCHEME_STORE_WRITTEN=false
WORKBENCH_MODIFIED=false
PROVIDER_CALLED=false
ZIP_PATHS_USE_FORWARD_SLASH=true
ZIP_ENTRY_COUNT=8
SHA256=42a81cfb698b3a1d763e3a5db813df4b3d784bb518aa939768dddfac2bbd2939
NEXT_STAGE=0957B_FIELD_SCHEME_ACTIVATION_DRY_RUN_CONTRACT
NEXT_STAGE_REQUIRES_EXPLICIT_DECISION=true
```

### 0957B Field Scheme Activation Dry Run Contract

外部报告目录：

`D:\Documents\SmartEdu\xiaobei-core-external-reports\0957B_FIELD_SCHEME_ACTIVATION_DRY_RUN_CONTRACT_20260607_053750`

项目内轻量产物：

- `docs/foundation/field_scheme_activation_dry_run_contract_0957B.md`
- `docs/foundation/field_scheme_activation_dry_run_contract_0957B.json`
- `scripts/validate_field_scheme_activation_dry_run_contract_0957B.py`

外部审核包：

`D:\Documents\SmartEdu\xiaobei-core-external-reports\0957B_FIELD_SCHEME_ACTIVATION_DRY_RUN_CONTRACT_20260607_053750\0957B_field_scheme_activation_dry_run_contract_review_package.zip`

状态：

```text
0957B_FIELD_SCHEME_ACTIVATION_DRY_RUN_CONTRACT=CONTRACT_PASS
DRY_RUN_CONTRACT_DEFINED=true
DRY_RUN_EXECUTED=false
ACTIVATION_DECISION_CREATED=false
ACTIVE_SCHEME_CREATED=false
DEFAULT_SCHEME_WRITTEN=false
REQUIRED_DRY_RUN_CHECKS_COUNT=10
DRY_RUN_OUTPUT_STATUS_COUNT=8
ORDINARY_TEACHER_MUST_NOT_APPROVE_ACTIVATION=true
ADMINISTRATOR_CONFIRMATION_REQUIRED_FOR_REAL_ACTIVATION=true
AGENT_CAN_ACTIVATE=false
ACTIVE_FIELD_SCHEME_CREATED=false
REGISTRY_STORE_WRITTEN=false
FIELD_SCHEME_STORE_WRITTEN=false
WORKBENCH_MODIFIED=false
PROVIDER_CALLED=false
ZIP_PATHS_USE_FORWARD_SLASH=true
ZIP_ENTRY_COUNT=8
SHA256=76e4f09a6a80ae1e144034a093128a47c9fdea1ae4ba390f7b9a361c0f55840c
NEXT_STAGE=0957C_FIELD_SCHEME_ACTIVATION_DRY_RUN_FIXTURE_CONTRACT
NEXT_STAGE_REQUIRES_EXPLICIT_DECISION=true
```

### 0957C Field Scheme Activation Dry Run Fixture Contract

外部报告目录：

`D:\Documents\SmartEdu\xiaobei-core-external-reports\0957C_FIELD_SCHEME_ACTIVATION_DRY_RUN_FIXTURE_CONTRACT_20260607_054530`

项目内轻量产物：

- `docs/foundation/field_scheme_activation_dry_run_fixture_contract_0957C.md`
- `docs/foundation/field_scheme_activation_dry_run_fixture_contract_0957C.json`
- `docs/foundation/field_scheme_activation_dry_run_fixture_schema_0957C.json`
- `samples/field_scheme_activation_0957C/*.json`
- `scripts/validate_field_scheme_activation_dry_run_fixture_contract_0957C.py`

外部审核包：

`D:\Documents\SmartEdu\xiaobei-core-external-reports\0957C_FIELD_SCHEME_ACTIVATION_DRY_RUN_FIXTURE_CONTRACT_20260607_054530\0957C_field_scheme_activation_dry_run_fixture_contract_review_package.zip`

状态：

```text
0957C_FIELD_SCHEME_ACTIVATION_DRY_RUN_FIXTURE_CONTRACT=CONTRACT_PASS
FIXTURE_COUNT=6
COVERED_STATUSES=eligible_preview,blocked_by_permission,blocked_by_conflict,blocked_by_missing_rollback,blocked_by_missing_audit_record,blocked_by_teacher_summary_gap
SYNTHETIC_DATA_ONLY=true
DRY_RUN_EXECUTED=false
ACTIVE_FIELD_SCHEME_CREATED=false
REGISTRY_STORE_WRITTEN=false
FIELD_SCHEME_STORE_WRITTEN=false
WORKBENCH_MODIFIED=false
PROVIDER_CALLED=false
ZIP_PATHS_USE_FORWARD_SLASH=true
ZIP_ENTRY_COUNT=15
SHA256=f672260190d17690e77dfa9f5bd7e4fb703524765ae0e7e93f2b90fdf2f819e3
NEXT_STAGE=0957D_FIELD_SCHEME_ACTIVATION_DRY_RUN_READONLY_APPLY
NEXT_STAGE_REQUIRES_EXPLICIT_DECISION=true
```

### 0957D Field Scheme Activation Dry Run Readonly Apply

外部报告目录：

`D:\Documents\SmartEdu\xiaobei-core-external-reports\0957D_FIELD_SCHEME_ACTIVATION_DRY_RUN_READONLY_APPLY_20260607_055421`

项目内轻量产物：

- `docs/foundation/field_scheme_activation_dry_run_readonly_apply_0957D.md`
- `docs/foundation/field_scheme_activation_dry_run_readonly_apply_0957D.json`
- `scripts/field_scheme_activation_dry_run_readonly_mapper_0957D.py`
- `outputs/field_scheme_activation_0957D/activation_dry_run_preview_results_0957D.json`
- `scripts/validate_field_scheme_activation_dry_run_readonly_apply_0957D.py`

外部审核包：

`D:\Documents\SmartEdu\xiaobei-core-external-reports\0957D_FIELD_SCHEME_ACTIVATION_DRY_RUN_READONLY_APPLY_20260607_055421\0957D_field_scheme_activation_dry_run_readonly_apply_review_package.zip`

状态：

```text
0957D_FIELD_SCHEME_ACTIVATION_DRY_RUN_READONLY_APPLY=PASS
READONLY_APPLY_PERFORMED=true
RESULT_COUNT=6
ELIGIBLE_PREVIEW_COUNT=1
BLOCKED_PREVIEW_COUNT=5
DRY_RUN_EXECUTED=false
ACTIVE_FIELD_SCHEME_CREATED=false
ACTIVATION_DECISION_CREATED=false
REGISTRY_STORE_WRITTEN=false
FIELD_SCHEME_STORE_WRITTEN=false
WORKBENCH_MODIFIED=false
PROVIDER_CALLED=false
ZIP_PATHS_USE_FORWARD_SLASH=true
ZIP_ENTRY_COUNT=16
SHA256=2ae20f21b26636248ce569215b1c379b4e9a67865e0e924be32d6232d3dfa4aa
NEXT_STAGE=0957E_FIELD_SCHEME_ACTIVATION_DRY_RUN_READONLY_SMOKE
NEXT_STAGE_REQUIRES_EXPLICIT_DECISION=true
```

### 0957E Field Scheme Activation Dry Run Readonly Smoke

外部报告目录：

`D:\Documents\SmartEdu\xiaobei-core-external-reports\0957E_FIELD_SCHEME_ACTIVATION_DRY_RUN_READONLY_SMOKE_20260607_060122`

项目内轻量产物：

- `docs/foundation/field_scheme_activation_dry_run_readonly_smoke_0957E.md`
- `docs/foundation/field_scheme_activation_dry_run_readonly_smoke_0957E.json`
- `scripts/validate_field_scheme_activation_dry_run_readonly_smoke_0957E.py`

外部审核包：

`D:\Documents\SmartEdu\xiaobei-core-external-reports\0957E_FIELD_SCHEME_ACTIVATION_DRY_RUN_READONLY_SMOKE_20260607_060122\0957E_field_scheme_activation_dry_run_readonly_smoke_review_package.zip`

状态：

```text
0957E_FIELD_SCHEME_ACTIVATION_DRY_RUN_READONLY_SMOKE=PASS
RESULT_COUNT=6
ELIGIBLE_PREVIEW_COUNT=1
BLOCKED_PREVIEW_COUNT=5
ALL_PREVIEW_EFFECTS_READONLY_ONLY=true
ADMIN_REQUIRED_CHECKS_COUNT=10
AGENT_CAN_ACTIVATE=false
ORDINARY_TEACHER_MUST_NOT_APPROVE_ACTIVATION=true
DRY_RUN_EXECUTED=false
ACTIVE_FIELD_SCHEME_CREATED=false
REGISTRY_STORE_WRITTEN=false
FIELD_SCHEME_STORE_WRITTEN=false
WORKBENCH_MODIFIED=false
PROVIDER_CALLED=false
ZIP_PATHS_USE_FORWARD_SLASH=true
ZIP_ENTRY_COUNT=9
SHA256=d7241fa6f61181f5f69cfff43344b11b3ed6696d023dbc927266dbf8afa82017
NEXT_STAGE=0957F_FIELD_SCHEME_ACTIVATION_DRY_RUN_SEAL
NEXT_STAGE_REQUIRES_EXPLICIT_DECISION=true
```

### 0957F Field Scheme Activation Dry Run Seal

外部报告目录：

`D:\Documents\SmartEdu\xiaobei-core-external-reports\0957F_FIELD_SCHEME_ACTIVATION_DRY_RUN_SEAL_20260607_061337`

项目内轻量产物：

- `docs/foundation/field_scheme_activation_dry_run_seal_0957F.md`
- `docs/foundation/field_scheme_activation_dry_run_seal_0957F.json`
- `scripts/validate_field_scheme_activation_dry_run_seal_0957F.py`

外部审核包：

`D:\Documents\SmartEdu\xiaobei-core-external-reports\0957F_FIELD_SCHEME_ACTIVATION_DRY_RUN_SEAL_20260607_061337\0957F_field_scheme_activation_dry_run_seal_review_package.zip`

状态：

```text
0957F_FIELD_SCHEME_ACTIVATION_DRY_RUN_SEAL=SEALED
SEALED_CHAIN=0957A,0957B,0957C,0957D,0957E
FIXTURE_COUNT=6
RESULT_COUNT=6
ELIGIBLE_PREVIEW_COUNT=1
BLOCKED_PREVIEW_COUNT=5
ALL_PREVIEW_EFFECTS_READONLY_ONLY=true
ADMIN_REQUIRED_CHECKS_COUNT=10
AGENT_CAN_ACTIVATE=false
ORDINARY_TEACHER_MUST_NOT_APPROVE_ACTIVATION=true
ACTIVE_FIELD_SCHEME_CREATED=false
REGISTRY_STORE_WRITTEN=false
FIELD_SCHEME_STORE_WRITTEN=false
WORKBENCH_MODIFIED=false
PROVIDER_CALLED=false
ZIP_PATHS_USE_FORWARD_SLASH=true
ZIP_ENTRY_COUNT=13
SHA256=24d137950f1bb45c7a09fc64140b5c9de1303ef5b1fe7ea416fc8e22fe21a689
NEXT_STAGE=0957G_FIELD_SCHEME_PRESET_LIBRARY_SCOPE_CONTRACT
NEXT_STAGE_REQUIRES_EXPLICIT_DECISION=true
```

### 0957G Field Scheme Preset Library Scope Contract

外部报告目录：

`D:\Documents\SmartEdu\xiaobei-core-external-reports\0957G_FIELD_SCHEME_PRESET_LIBRARY_SCOPE_CONTRACT_20260607_062127`

项目内轻量产物：

- `docs/foundation/field_scheme_preset_library_scope_contract_0957G.md`
- `docs/foundation/field_scheme_preset_library_scope_contract_0957G.json`
- `scripts/validate_field_scheme_preset_library_scope_contract_0957G.py`

外部审核包：

`D:\Documents\SmartEdu\xiaobei-core-external-reports\0957G_FIELD_SCHEME_PRESET_LIBRARY_SCOPE_CONTRACT_20260607_062127\0957G_field_scheme_preset_library_scope_contract_review_package.zip`

状态：

```text
0957G_FIELD_SCHEME_PRESET_LIBRARY_SCOPE_CONTRACT=CONTRACT_PASS
PRESET_SCHEME_CANDIDATE_ALLOWED=true
SYSTEM_DEFAULT_PRESET_CANDIDATE_ALLOWED=true
TEACHER_CUSTOM_TEMPLATE_CANDIDATE_ALLOWED=true
AGENT_RECOMMENDATION_PREVIEW_ALLOWED=true
PUBLISHED_PRESET_SCHEME_CREATED=false
ACTIVE_PRESET_SCHEME_CREATED=false
ACTIVE_FIELD_SCHEME_CREATED=false
ORDINARY_TEACHER_CAN_SELECT_PRESET_PREVIEW=true
ORDINARY_TEACHER_CAN_PUBLISH_PRESET=false
ORDINARY_TEACHER_CAN_ACTIVATE_PRESET=false
ADVANCED_TEACHER_CAN_ADJUST_TEMPLATE_CANDIDATE=true
ADMINISTRATOR_CAN_PUBLISH_FUTURE_GATE_ONLY=true
AGENT_CAN_RECOMMEND_PRESET=true
AGENT_CAN_PUBLISH_PRESET=false
AGENT_CAN_ACTIVATE_PRESET=false
FUTURE_MEMORY_REFERENCE_POSSIBLE=true
MEMORY_INTEGRATION_NOW=false
MEMORY_STORE_WRITTEN=false
RETRIEVAL_ENABLED=false
PROVIDER_CONTEXT_INJECTION=false
WORKBENCH_MODIFIED=false
ZIP_PATHS_USE_FORWARD_SLASH=true
ZIP_ENTRY_COUNT=8
SHA256=7360325022b76157be1b3bb7e004977aa129481a9117a2ba30b95f9ff5948722
NEXT_STAGE=0957H_FIELD_SCHEME_PRESET_LIBRARY_SCHEMA_CONTRACT
NEXT_STAGE_REQUIRES_EXPLICIT_DECISION=true
```

### 0957H Field Scheme Preset Library Schema Contract

外部报告目录：

`D:\Documents\SmartEdu\xiaobei-core-external-reports\0957H_FIELD_SCHEME_PRESET_LIBRARY_SCHEMA_CONTRACT_20260607_062647`

项目内轻量产物：

- `docs/foundation/field_scheme_preset_library_schema_contract_0957H.md`
- `docs/foundation/field_scheme_preset_library_schema_contract_0957H.json`
- `docs/foundation/field_scheme_preset_library_schema_0957H.json`
- `scripts/validate_field_scheme_preset_library_schema_contract_0957H.py`

外部审核包：

`D:\Documents\SmartEdu\xiaobei-core-external-reports\0957H_FIELD_SCHEME_PRESET_LIBRARY_SCHEMA_CONTRACT_20260607_062647\0957H_field_scheme_preset_library_schema_contract_review_package.zip`

状态：

```text
0957H_FIELD_SCHEME_PRESET_LIBRARY_SCHEMA_CONTRACT=CONTRACT_PASS
SCHEMA_FILE=docs/foundation/field_scheme_preset_library_schema_0957H.json
REQUIRED_FIELD_COUNT=17
PRESET_TYPE_COUNT=4
PRESET_STATUS_COUNT=7
ROLE_VISIBILITY_REQUIRED=true
AGENT_RECOMMENDATION_POLICY_REQUIRED=true
ACTIVATION_GATE_REQUIRED=true
MEMORY_REFERENCE_BOUNDARY_REQUIRED=true
MEMORY_INTEGRATION_NOW=false
PRESET_ENTRIES_CREATED=false
REAL_PRESET_LIBRARY_CREATED=false
ACTIVE_PRESET_SCHEME_CREATED=false
PUBLISHED_PRESET_SCHEME_CREATED=false
REGISTRY_STORE_WRITTEN=false
WORKBENCH_MODIFIED=false
PROVIDER_CALLED=false
ZIP_PATHS_USE_FORWARD_SLASH=true
ZIP_ENTRY_COUNT=9
SHA256=a429a787af1e24f3201735f8ddcb45e6ba826f3b38518bd79c4f4cfe9a3107c7
NEXT_STAGE=0957I_FIELD_SCHEME_PRESET_LIBRARY_FIXTURE_CONTRACT
NEXT_STAGE_REQUIRES_EXPLICIT_DECISION=true
```

### 0957I Field Scheme Preset Library Fixture Contract

外部报告目录：

`D:\Documents\SmartEdu\xiaobei-core-external-reports\0957I_FIELD_SCHEME_PRESET_LIBRARY_FIXTURE_CONTRACT_20260607_063424`

项目内轻量产物：

- `docs/foundation/field_scheme_preset_library_fixture_contract_0957I.md`
- `docs/foundation/field_scheme_preset_library_fixture_contract_0957I.json`
- `samples/field_scheme_preset_library_0957I/*.json`
- `scripts/validate_field_scheme_preset_library_fixture_contract_0957I.py`

外部审核包：

`D:\Documents\SmartEdu\xiaobei-core-external-reports\0957I_FIELD_SCHEME_PRESET_LIBRARY_FIXTURE_CONTRACT_20260607_063424\0957I_field_scheme_preset_library_fixture_contract_review_package.zip`

状态：

```text
0957I_FIELD_SCHEME_PRESET_LIBRARY_FIXTURE_CONTRACT=CONTRACT_PASS
LEGAL_FIXTURE_COUNT=4
INVALID_FIXTURE_COUNT=1
LEGAL_PRESET_TYPES=system_default_preset_candidate,teacher_custom_template_candidate,agent_generated_template_candidate,administrator_curated_preset_candidate
INVALID_FIXTURE_REJECTED=true
ACTIVE_OR_PUBLISHED_STATUS_REJECTED=true
SYNTHETIC_DATA_ONLY=true
PRESET_ENTRIES_CREATED=false
REAL_PRESET_LIBRARY_CREATED=false
ACTIVE_PRESET_SCHEME_CREATED=false
PUBLISHED_PRESET_SCHEME_CREATED=false
REGISTRY_STORE_WRITTEN=false
WORKBENCH_MODIFIED=false
PROVIDER_CALLED=false
MEMORY_STORE_WRITTEN=false
ZIP_PATHS_USE_FORWARD_SLASH=true
ZIP_ENTRY_COUNT=14
SHA256=22436cad326d193f834f58674fc199f8f45b163327e200e480cebcb4680e7be7
NEXT_STAGE=0957J_FIELD_SCHEME_PRESET_LIBRARY_FIXTURE_SMOKE
NEXT_STAGE_REQUIRES_EXPLICIT_DECISION=true
```

### 0957J Field Scheme Preset Library Fixture Smoke

外部报告目录：

`D:\Documents\SmartEdu\xiaobei-core-external-reports\0957J_FIELD_SCHEME_PRESET_LIBRARY_FIXTURE_SMOKE_20260607_064305`

项目内轻量产物：

- `docs/foundation/field_scheme_preset_library_fixture_smoke_0957J.md`
- `docs/foundation/field_scheme_preset_library_fixture_smoke_0957J.json`
- `scripts/validate_field_scheme_preset_library_fixture_smoke_0957J.py`

外部审核包：

`D:\Documents\SmartEdu\xiaobei-core-external-reports\0957J_FIELD_SCHEME_PRESET_LIBRARY_FIXTURE_SMOKE_20260607_064305\0957J_field_scheme_preset_library_fixture_smoke_review_package.zip`

状态：

```text
0957J_FIELD_SCHEME_PRESET_LIBRARY_FIXTURE_SMOKE=PASS
LEGAL_FIXTURE_COUNT=4
INVALID_FIXTURE_COUNT=1
LEGAL_FIXTURES_SCHEMA_PASS=true
INVALID_FIXTURE_REJECTED=true
ACTIVE_OR_PUBLISHED_STATUS_REJECTED=true
SYNTHETIC_DATA_ONLY=true
READONLY_PREVIEW_OUTPUT_CREATED=false
PRESET_ENTRIES_CREATED=false
REAL_PRESET_LIBRARY_CREATED=false
ACTIVE_PRESET_SCHEME_CREATED=false
PUBLISHED_PRESET_SCHEME_CREATED=false
REGISTRY_STORE_WRITTEN=false
WORKBENCH_MODIFIED=false
PROVIDER_CALLED=false
MEMORY_STORE_WRITTEN=false
ZIP_PATHS_USE_FORWARD_SLASH=true
ZIP_ENTRY_COUNT=14
SHA256=32991f03fda952f2b7c7e493a32752ecbbadb6340b481cf0f7a33c06f8ab1a3a
NEXT_STAGE=0957K_FIELD_SCHEME_PRESET_LIBRARY_READONLY_PREVIEW_CONTRACT
NEXT_STAGE_REQUIRES_EXPLICIT_DECISION=true
```

### 0957K-0957N Field Scheme Preset Library Readonly Preview And V0 Seal

外部报告目录：

- `D:\Documents\SmartEdu\xiaobei-core-external-reports\0957K_FIELD_SCHEME_PRESET_LIBRARY_READONLY_PREVIEW_CONTRACT_20260607_065417`
- `D:\Documents\SmartEdu\xiaobei-core-external-reports\0957L_FIELD_SCHEME_PRESET_LIBRARY_READONLY_PREVIEW_APPLY_20260607_065418`
- `D:\Documents\SmartEdu\xiaobei-core-external-reports\0957M_FIELD_SCHEME_PRESET_LIBRARY_READONLY_PREVIEW_SMOKE_20260607_065418`
- `D:\Documents\SmartEdu\xiaobei-core-external-reports\0957N_FIELD_SCHEME_PRESET_LIBRARY_V0_SEAL_20260607_065419`

项目内轻量产物：

- `docs/foundation/field_scheme_preset_library_readonly_preview_contract_0957K.*`
- `docs/foundation/field_scheme_preset_library_readonly_preview_apply_0957L.*`
- `docs/foundation/field_scheme_preset_library_readonly_preview_smoke_0957M.*`
- `docs/foundation/field_scheme_preset_library_v0_seal_0957N.*`
- `scripts/field_scheme_preset_library_readonly_preview_mapper_0957L.py`
- `scripts/validate_field_scheme_preset_library_readonly_preview_contract_0957K.py`
- `scripts/validate_field_scheme_preset_library_readonly_preview_apply_0957L.py`
- `scripts/validate_field_scheme_preset_library_readonly_preview_smoke_0957M.py`
- `scripts/validate_field_scheme_preset_library_v0_seal_0957N.py`
- `outputs/field_scheme_preset_library_0957L/*.json`

外部审核包：

- `D:\Documents\SmartEdu\xiaobei-core-external-reports\0957K_FIELD_SCHEME_PRESET_LIBRARY_READONLY_PREVIEW_CONTRACT_20260607_065417\0957K_field_scheme_preset_library_readonly_preview_contract_review_package.zip`
- `D:\Documents\SmartEdu\xiaobei-core-external-reports\0957L_FIELD_SCHEME_PRESET_LIBRARY_READONLY_PREVIEW_APPLY_20260607_065418\0957L_field_scheme_preset_library_readonly_preview_apply_review_package.zip`
- `D:\Documents\SmartEdu\xiaobei-core-external-reports\0957M_FIELD_SCHEME_PRESET_LIBRARY_READONLY_PREVIEW_SMOKE_20260607_065418\0957M_field_scheme_preset_library_readonly_preview_smoke_review_package.zip`
- `D:\Documents\SmartEdu\xiaobei-core-external-reports\0957N_FIELD_SCHEME_PRESET_LIBRARY_V0_SEAL_20260607_065419\0957N_field_scheme_preset_library_v0_seal_review_package.zip`

状态：

```text
0957K_FIELD_SCHEME_PRESET_LIBRARY_READONLY_PREVIEW_CONTRACT=CONTRACT_PASS
0957L_FIELD_SCHEME_PRESET_LIBRARY_READONLY_PREVIEW_APPLY=PASS
0957M_FIELD_SCHEME_PRESET_LIBRARY_READONLY_PREVIEW_SMOKE=PASS
0957N_FIELD_SCHEME_PRESET_LIBRARY_V0_SEAL=SEALED
FIELD_SCHEME_PRESET_LIBRARY_V0=SEALED
PREVIEW_COUNT=4
REJECTED_COUNT=1
READONLY_PREVIEW_OUTPUT_CREATED=true
REAL_PRESET_LIBRARY_CREATED=false
PRESET_ENTRIES_CREATED=false
ACTIVE_PRESET_SCHEME_CREATED=false
PUBLISHED_PRESET_SCHEME_CREATED=false
REGISTRY_STORE_WRITTEN=false
WORKBENCH_MODIFIED=false
PROVIDER_CALLED=false
MEMORY_STORE_WRITTEN=false
0957K_ZIP_ENTRY_COUNT=8
0957K_SHA256=f0536b403a029f32e24e61d375ac9bd2935a6d2382e2d645396e41d8ff0f2368
0957L_ZIP_ENTRY_COUNT=11
0957L_SHA256=dae9946aff1ab74a2c083165c6729c7066274bf35ccb9f26e1616444312957b5
0957M_ZIP_ENTRY_COUNT=10
0957M_SHA256=3ceecfb8c5e26fb84a9a1f307fb0d1e83a7de04247feb850d5cbb3a482b3593f
0957N_ZIP_ENTRY_COUNT=10
0957N_SHA256=e3315ccd87a8139f38baa7fe1d9d17bd5b64bded438cf41057fdac463339f708
ZIP_PATHS_USE_FORWARD_SLASH=true
TEMP_ISOLATED_REVIEW_TREE_PASS=true
NEXT_STAGE=0958A_PRESET_LIBRARY_ACTIVATION_GATE_SCOPE_CONTRACT
NEXT_STAGE_REQUIRES_EXPLICIT_DECISION=true
```

### 0958A-0958F Preset Library Activation Gate V0

外部报告目录：

- `D:\Documents\SmartEdu\xiaobei-core-external-reports\0958A_PRESET_LIBRARY_ACTIVATION_GATE_SCOPE_CONTRACT_20260607_071243`
- `D:\Documents\SmartEdu\xiaobei-core-external-reports\0958B_PRESET_LIBRARY_ACTIVATION_GATE_SCHEMA_CONTRACT_20260607_071243`
- `D:\Documents\SmartEdu\xiaobei-core-external-reports\0958C_PRESET_LIBRARY_ACTIVATION_GATE_FIXTURE_CONTRACT_20260607_071243`
- `D:\Documents\SmartEdu\xiaobei-core-external-reports\0958D_PRESET_LIBRARY_ACTIVATION_GATE_DRY_RUN_APPLY_20260607_071243`
- `D:\Documents\SmartEdu\xiaobei-core-external-reports\0958E_PRESET_LIBRARY_ACTIVATION_GATE_SMOKE_20260607_071243`
- `D:\Documents\SmartEdu\xiaobei-core-external-reports\0958F_PRESET_LIBRARY_ACTIVATION_GATE_SEAL_20260607_071243`

状态：

```text
0958A_PRESET_LIBRARY_ACTIVATION_GATE_SCOPE_CONTRACT=CONTRACT_PASS
0958B_PRESET_LIBRARY_ACTIVATION_GATE_SCHEMA_CONTRACT=CONTRACT_PASS
0958C_PRESET_LIBRARY_ACTIVATION_GATE_FIXTURE_CONTRACT=CONTRACT_PASS
0958D_PRESET_LIBRARY_ACTIVATION_GATE_DRY_RUN_APPLY=PASS
0958E_PRESET_LIBRARY_ACTIVATION_GATE_SMOKE=PASS
0958F_PRESET_LIBRARY_ACTIVATION_GATE_SEAL=SEALED
PRESET_LIBRARY_ACTIVATION_GATE_V0=SEALED
ELIGIBLE_COUNT=1
BLOCKED_COUNT=5
REAL_REGISTRY_ENTRY_CREATED=false
PRESET_LIBRARY_STORE_WRITTEN=false
REGISTRY_STORE_WRITTEN=false
WORKBENCH_MODIFIED=false
PROVIDER_CALLED=false
MEMORY_STORE_WRITTEN=false
AGENT_PUBLISHED=false
AGENT_ACTIVATED=false
ORDINARY_TEACHER_ACTIVATED=false
0958A_ZIP_ENTRY_COUNT=7
0958A_SHA256=5f66fd64f02e87039c4739a0af88fee19f94b89b3bdfd2a1ca98086ae675219e
0958B_ZIP_ENTRY_COUNT=8
0958B_SHA256=32b960801f77edc75ad6b2b6e3a98e15e1dcea8672cbb141389fb29fe2aa2fd6
0958C_ZIP_ENTRY_COUNT=13
0958C_SHA256=ee79dbaf25aec3bc41327ede548fe661075cfa4285bc96da525cb19e4f7d0d8a
0958D_ZIP_ENTRY_COUNT=8
0958D_SHA256=6676eecb86ca8014db07d8e9e69ec8b30481d697488404074bcb2e46e28eccf0
0958E_ZIP_ENTRY_COUNT=8
0958E_SHA256=0bf95061b69e7505c826e1cf6527d6fe62d2765669f8649c789f9ef865e4ade3
0958F_ZIP_ENTRY_COUNT=8
0958F_SHA256=afd6a3a39410222de73ece4f9f9ab81529b8d3778ab6040cdb2c39efe65b96b3
ZIP_PATHS_USE_FORWARD_SLASH=true
TEMP_ISOLATED_REVIEW_TREE_PASS=true
NEXT_STAGE=0959A_PRESET_LIBRARY_REGISTRY_READONLY_APPLY_OR_HOLD_GATE
NEXT_STAGE_REQUIRES_EXPLICIT_DECISION=true
```

### 0959A-0959E Preset Library Registry Readonly V0

外部报告目录：

- `D:\Documents\SmartEdu\xiaobei-core-external-reports\0959A_PRESET_LIBRARY_REGISTRY_READONLY_APPLY_OR_HOLD_GATE_20260607_071922`
- `D:\Documents\SmartEdu\xiaobei-core-external-reports\0959B_PRESET_LIBRARY_REGISTRY_READONLY_SCHEMA_CONTRACT_20260607_071922`
- `D:\Documents\SmartEdu\xiaobei-core-external-reports\0959C_PRESET_LIBRARY_REGISTRY_READONLY_CANDIDATE_APPLY_20260607_071922`
- `D:\Documents\SmartEdu\xiaobei-core-external-reports\0959D_PRESET_LIBRARY_REGISTRY_READONLY_CANDIDATE_SMOKE_20260607_071922`
- `D:\Documents\SmartEdu\xiaobei-core-external-reports\0959E_PRESET_LIBRARY_REGISTRY_READONLY_V0_SEAL_20260607_071922`

状态：

```text
0959A_PRESET_LIBRARY_REGISTRY_READONLY_APPLY_OR_HOLD_GATE=PASS
0959B_PRESET_LIBRARY_REGISTRY_READONLY_SCHEMA_CONTRACT=CONTRACT_PASS
0959C_PRESET_LIBRARY_REGISTRY_READONLY_CANDIDATE_APPLY=PASS
0959D_PRESET_LIBRARY_REGISTRY_READONLY_CANDIDATE_SMOKE=PASS
0959E_PRESET_LIBRARY_REGISTRY_READONLY_V0_SEAL=SEALED
PRESET_LIBRARY_REGISTRY_READONLY_V0=SEALED
CANDIDATE_COUNT=1
EXCLUDED_COUNT=5
REAL_REGISTRY_ENTRY_CREATED=false
REGISTRY_STORE_WRITTEN=false
PRESET_LIBRARY_STORE_WRITTEN=false
WORKBENCH_MODIFIED=false
FRONTEND_MODIFIED=false
BACKEND_MODIFIED=false
RUNTIME_MODIFIED=false
ENDPOINT_CREATED=false
PROVIDER_CALLED=false
MEMORY_STORE_WRITTEN=false
ACTIVE_PRESET_SCHEME_CREATED=false
PUBLISHED_PRESET_SCHEME_CREATED=false
0959A_ZIP_ENTRY_COUNT=9
0959A_SHA256=6e3ad3b792896190e8bb781a9d40fa1ed362edea0a9168bbbb72f2fd380cb127
0959B_ZIP_ENTRY_COUNT=9
0959B_SHA256=65232de0a42c46722dfe689243670c95dea440a8c0623490fab2109cdb5ae8a4
0959C_ZIP_ENTRY_COUNT=10
0959C_SHA256=35b77d7ee9456d54778a0551316e0da3a0b9078896d88a078ae75bde616c7593
0959D_ZIP_ENTRY_COUNT=10
0959D_SHA256=a221e3ca894e0a5b2280e1de1eb3e5e769b6ab7ebcb3cfa1077fd5108507988d
0959E_ZIP_ENTRY_COUNT=10
0959E_SHA256=22bffbe31867812e416a25ac5e479d0b23fe9d6ecbd06581e1f4cb8838d0e869
ZIP_PATHS_USE_FORWARD_SLASH=true
TEMP_ISOLATED_REVIEW_TREE_PASS=true
NEXT_STAGE=0960A_PRESET_LIBRARY_WORKBENCH_READONLY_BINDING_OR_HOLD_GATE
NEXT_STAGE_REQUIRES_EXPLICIT_DECISION=true
```

### 0960A-0960E Preset Library Workbench Readonly Binding V0

外部报告目录：

- `D:\Documents\SmartEdu\xiaobei-core-external-reports\0960A_PRESET_LIBRARY_WORKBENCH_READONLY_BINDING_OR_HOLD_GATE_20260607_072548`
- `D:\Documents\SmartEdu\xiaobei-core-external-reports\0960B_PRESET_LIBRARY_WORKBENCH_READONLY_BINDING_SCHEMA_CONTRACT_20260607_072548`
- `D:\Documents\SmartEdu\xiaobei-core-external-reports\0960C_PRESET_LIBRARY_WORKBENCH_READONLY_BINDING_CANDIDATE_APPLY_20260607_072548`
- `D:\Documents\SmartEdu\xiaobei-core-external-reports\0960D_PRESET_LIBRARY_WORKBENCH_READONLY_BINDING_CANDIDATE_SMOKE_20260607_072548`
- `D:\Documents\SmartEdu\xiaobei-core-external-reports\0960E_PRESET_LIBRARY_WORKBENCH_READONLY_BINDING_V0_SEAL_20260607_072548`

项目内轻量产物：

- `docs/foundation/preset_library_workbench_readonly_binding_or_hold_gate_0960A.*`
- `docs/foundation/preset_library_workbench_readonly_binding_schema_contract_0960B.*`
- `docs/foundation/preset_library_workbench_readonly_binding_schema_0960B.json`
- `docs/foundation/preset_library_workbench_readonly_binding_candidate_apply_0960C.*`
- `docs/foundation/preset_library_workbench_readonly_binding_candidate_smoke_0960D.*`
- `docs/foundation/preset_library_workbench_readonly_binding_v0_seal_0960E.*`
- `outputs/preset_library_workbench_binding_0960C/*.json`
- `scripts/validate_preset_library_workbench_readonly_binding_*_0960*.py`

状态：

```text
0960A_PRESET_LIBRARY_WORKBENCH_READONLY_BINDING_OR_HOLD_GATE=PASS
0960B_PRESET_LIBRARY_WORKBENCH_READONLY_BINDING_SCHEMA_CONTRACT=CONTRACT_PASS
0960C_PRESET_LIBRARY_WORKBENCH_READONLY_BINDING_CANDIDATE_APPLY=PASS
0960D_PRESET_LIBRARY_WORKBENCH_READONLY_BINDING_CANDIDATE_SMOKE=PASS
0960E_PRESET_LIBRARY_WORKBENCH_READONLY_BINDING_V0_SEAL=SEALED
PRESET_LIBRARY_WORKBENCH_READONLY_BINDING_V0=SEALED
CANDIDATE_COUNT=1
EXCLUDED_COUNT=5
REAL_WORKBENCH_BINDING_CREATED=false
WORKBENCH_BINDING_STORE_WRITTEN=false
INDEX_HTML_MODIFIED=false
FRONTEND_RUNTIME_MODIFIED=false
FRONTEND_MODIFIED=false
BACKEND_MODIFIED=false
RUNTIME_MODIFIED=false
ENDPOINT_CREATED=false
ROUTE_CREATED=false
IMPORT_CREATED=false
PROVIDER_CALLED=false
MEMORY_STORE_WRITTEN=false
REGISTRY_STORE_WRITTEN=false
ACTIVE_PRESET_SCHEME_CREATED=false
PUBLISHED_PRESET_SCHEME_CREATED=false
0960A_ZIP_ENTRY_COUNT=7
0960A_SHA256=53ffe8e21fc187184e0c8013e0130b2d29e0a00c8532a616422cf4ee478c6ab7
0960B_ZIP_ENTRY_COUNT=8
0960B_SHA256=b61521d39d86c1192b7eca225b00f14bcba4eefc0fcf4a8b316277b1b002fb39
0960C_ZIP_ENTRY_COUNT=10
0960C_SHA256=aaf2d0dd97d54d67d7eac2dbfe2db4782dca3879b73ec608d48c538b5c5b4048
0960D_ZIP_ENTRY_COUNT=10
0960D_SHA256=ec4676784842332be33ddee4b31752caa237deaee0905d1f088c0481e400fa10
0960E_ZIP_ENTRY_COUNT=10
0960E_SHA256=77ba22839f452cce4f8cf2a77c79079a1923a9e4f0221b97f82c9945a0b52a17
ZIP_PATHS_USE_FORWARD_SLASH=true
TEMP_ISOLATED_REVIEW_TREE_PASS=true
NEXT_STAGE=0961A_PRESET_LIBRARY_WORKBENCH_VISIBLE_PREVIEW_OR_HOLD_GATE
NEXT_STAGE_REQUIRES_EXPLICIT_DECISION=true
```

### 0961A-0961E Preset Library Workbench Visible Preview Gate V0

外部报告目录：

- `D:\Documents\SmartEdu\xiaobei-core-external-reports\0961A_PRESET_LIBRARY_WORKBENCH_VISIBLE_PREVIEW_OR_HOLD_GATE_20260607_074120`
- `D:\Documents\SmartEdu\xiaobei-core-external-reports\0961B_PRESET_LIBRARY_WORKBENCH_VISIBLE_PREVIEW_VIEWMODEL_SCHEMA_CONTRACT_20260607_074120`
- `D:\Documents\SmartEdu\xiaobei-core-external-reports\0961C_PRESET_LIBRARY_WORKBENCH_VISIBLE_PREVIEW_READONLY_MOUNT_PREVIEW_20260607_074120`
- `D:\Documents\SmartEdu\xiaobei-core-external-reports\0961D_PRESET_LIBRARY_WORKBENCH_VISIBLE_PREVIEW_SMOKE_20260607_074120`
- `D:\Documents\SmartEdu\xiaobei-core-external-reports\0961E_PRESET_LIBRARY_WORKBENCH_VISIBLE_PREVIEW_GATE_SEAL_20260607_074120`

项目内轻量产物：

- `docs/foundation/preset_library_workbench_visible_preview_or_hold_gate_0961A.*`
- `docs/foundation/preset_library_workbench_visible_preview_viewmodel_schema_contract_0961B.*`
- `docs/foundation/preset_library_workbench_visible_preview_viewmodel_schema_0961B.json`
- `docs/foundation/preset_library_workbench_visible_preview_readonly_mount_preview_0961C.*`
- `docs/foundation/preset_library_workbench_visible_preview_smoke_0961D.*`
- `docs/foundation/preset_library_workbench_visible_preview_gate_seal_0961E.*`
- `outputs/preset_library_workbench_visible_preview_0961C/*.json`
- `scripts/validate_preset_library_workbench_visible_preview_*_0961*.py`

状态：

```text
0961A_PRESET_LIBRARY_WORKBENCH_VISIBLE_PREVIEW_OR_HOLD_GATE=PASS
0961B_PRESET_LIBRARY_WORKBENCH_VISIBLE_PREVIEW_VIEWMODEL_SCHEMA_CONTRACT=CONTRACT_PASS
0961C_PRESET_LIBRARY_WORKBENCH_VISIBLE_PREVIEW_READONLY_MOUNT_PREVIEW=PASS
0961D_PRESET_LIBRARY_WORKBENCH_VISIBLE_PREVIEW_SMOKE=PASS
0961E_PRESET_LIBRARY_WORKBENCH_VISIBLE_PREVIEW_GATE_SEAL=SEALED
PRESET_LIBRARY_WORKBENCH_VISIBLE_PREVIEW_GATE_V0=SEALED
VISIBLE_PREVIEW_CANDIDATE_COUNT=1
EXCLUDED_COUNT=5
VISIBLE_PREVIEW_APPLY_PERFORMED=false
VISIBLE_UI_APPLY_PERFORMED=false
REAL_VISIBLE_PREVIEW_CREATED=false
REAL_WORKBENCH_BINDING_CREATED=false
INDEX_HTML_MODIFIED=false
FRONTEND_RUNTIME_MODIFIED=false
FRONTEND_MODIFIED=false
BACKEND_MODIFIED=false
RUNTIME_MODIFIED=false
ENDPOINT_CREATED=false
ROUTE_CREATED=false
IMPORT_CREATED=false
COMPONENT_GRID_BEHAVIOR_CHANGED=false
PROVIDER_CALLED=false
MEMORY_STORE_WRITTEN=false
REGISTRY_STORE_WRITTEN=false
ACTIVE_PRESET_SCHEME_CREATED=false
PUBLISHED_PRESET_SCHEME_CREATED=false
0961A_ZIP_ENTRY_COUNT=7
0961A_SHA256=7f427f83902de06e91c8079e772db8617b4878b700da335b9f11a36bfdc4989b
0961B_ZIP_ENTRY_COUNT=8
0961B_SHA256=d4a64c9f3d04c9b1cd24489d11e344c043c6b6a530f7fed6f3bfce6fb10ce048
0961C_ZIP_ENTRY_COUNT=11
0961C_SHA256=f1514c59492b2a06f23a4dd84394b3c756ea617fd1bccdbad8ea7a02cc971169
0961D_ZIP_ENTRY_COUNT=11
0961D_SHA256=1658dabcc6ff227c20e24cb0dfe0ecc5a55e9631fe8a3ee2c0233a2108a16777
0961E_ZIP_ENTRY_COUNT=11
0961E_SHA256=1461533f67f0560c873baef0e151532c25c15bb3121289f318064b7cd108984a
ZIP_PATHS_USE_FORWARD_SLASH=true
TEMP_ISOLATED_REVIEW_TREE_PASS=true
NEXT_STAGE=0962A_WORKBENCH_PRESET_LIBRARY_VISIBLE_READONLY_APPLY_GATE
NEXT_STAGE_REQUIRES_EXPLICIT_DECISION=true
```

### 0962A-0962C Workbench Preset Library Visible Readonly Apply Gate And Contract

外部报告目录：

- `D:\Documents\SmartEdu\xiaobei-core-external-reports\0962A_WORKBENCH_PRESET_LIBRARY_VISIBLE_READONLY_APPLY_GATE_20260607_075122`
- `D:\Documents\SmartEdu\xiaobei-core-external-reports\0962B_WORKBENCH_PRESET_LIBRARY_TARGET_SURFACE_SCAN_20260607_075122`
- `D:\Documents\SmartEdu\xiaobei-core-external-reports\0962C_WORKBENCH_PRESET_LIBRARY_VISIBLE_READONLY_APPLY_CONTRACT_20260607_075122`

项目内轻量产物：

- `docs/foundation/workbench_preset_library_visible_readonly_apply_gate_0962A.*`
- `docs/foundation/workbench_preset_library_target_surface_scan_0962B.*`
- `docs/foundation/workbench_preset_library_visible_readonly_apply_contract_0962C.*`
- `docs/foundation/workbench_preset_library_visible_readonly_apply_contract_schema_0962C.json`
- `outputs/workbench_preset_library_visible_apply_0962B/workbench_target_surface_scan_0962B.json`
- `outputs/workbench_preset_library_visible_apply_0962C/visible_readonly_apply_contract_preview_0962C.json`
- `scripts/validate_workbench_preset_library_*_0962*.py`

状态：

```text
0962A_WORKBENCH_PRESET_LIBRARY_VISIBLE_READONLY_APPLY_GATE=PASS
0962B_WORKBENCH_PRESET_LIBRARY_TARGET_SURFACE_SCAN=PASS
0962C_WORKBENCH_PRESET_LIBRARY_VISIBLE_READONLY_APPLY_CONTRACT=CONTRACT_PASS
PRIMARY_TARGET=frontend/workbench/index.html
MOUNT_ANCHOR=<div class="component-grid doc-scroll" id="componentGrid">
RECOMMENDED_INSERT_POSITION=after article[data-card="packageCheck"] and before div.extra-toggle
COMPONENT_DATA_CARD=presetLibraryReadonly
VISIBLE_READONLY_APPLY_PERFORMED=false
UI_PATCH_CREATED=false
UI_PATCH_APPLIED=false
VISIBLE_UI_APPLY_PERFORMED=false
REAL_VISIBLE_PREVIEW_CREATED=false
INDEX_HTML_MODIFIED=false
FRONTEND_WORKBENCH_INDEX_MODIFIED=false
FRONTEND_RUNTIME_MODIFIED=false
ROUTE_CREATED=false
IMPORT_CREATED=false
BACKEND_MODIFIED=false
ENDPOINT_CREATED=false
PROVIDER_CALLED=false
MEMORY_STORE_WRITTEN=false
REGISTRY_STORE_WRITTEN=false
0962A_ZIP_ENTRY_COUNT=7
0962A_SHA256=70730fa332c446fd7a5596f94986dd5049025ccf03c32625cca5c03746767746
0962B_ZIP_ENTRY_COUNT=8
0962B_SHA256=649344ace97c5ace57e1a91c46508eed18c1c484d45e01946fd3bebc2c382310
0962C_ZIP_ENTRY_COUNT=10
0962C_SHA256=2a923991dabdd323a7f325995eb767ec0e3f5ede2ca8f52f962ed12c892c7c45
ZIP_PATHS_USE_FORWARD_SLASH=true
TEMP_ISOLATED_REVIEW_TREE_PASS=true
NEXT_STAGE=0962D_WORKBENCH_PRESET_LIBRARY_VISIBLE_READONLY_UI_PATCH_CANDIDATE
NEXT_STAGE_REQUIRES_EXPLICIT_DECISION=true
```

### 0962D-0962F Workbench Preset Library Visible Readonly UI Patch Candidate Pack

外部报告目录：

- `D:\Documents\SmartEdu\xiaobei-core-external-reports\0962D_WORKBENCH_PRESET_LIBRARY_VISIBLE_READONLY_UI_PATCH_CANDIDATE_20260607_075742`
- `D:\Documents\SmartEdu\xiaobei-core-external-reports\0962E_WORKBENCH_PRESET_LIBRARY_VISIBLE_READONLY_UI_PATCH_CANDIDATE_SMOKE_20260607_075742`
- `D:\Documents\SmartEdu\xiaobei-core-external-reports\0962F_WORKBENCH_PRESET_LIBRARY_VISIBLE_READONLY_APPLY_OR_HOLD_GATE_20260607_075742`

项目内轻量产物：

- `docs/foundation/workbench_preset_library_visible_readonly_ui_patch_candidate_0962D.*`
- `docs/foundation/workbench_preset_library_visible_readonly_ui_patch_candidate_smoke_0962E.*`
- `docs/foundation/workbench_preset_library_visible_readonly_apply_or_hold_gate_0962F.*`
- `outputs/workbench_preset_library_visible_apply_0962D/ui_patch_candidate_0962D.json`
- `outputs/workbench_preset_library_visible_apply_0962D/ui_patch_candidate_preview_0962D.html`
- `outputs/workbench_preset_library_visible_apply_0962E/ui_patch_candidate_smoke_0962E.json`
- `outputs/workbench_preset_library_visible_apply_0962F/apply_or_hold_gate_0962F.json`
- `scripts/validate_workbench_preset_library_visible_readonly_*_0962*.py`

状态：

```text
0962D_WORKBENCH_PRESET_LIBRARY_VISIBLE_READONLY_UI_PATCH_CANDIDATE=PASS
0962E_WORKBENCH_PRESET_LIBRARY_VISIBLE_READONLY_UI_PATCH_CANDIDATE_SMOKE=PASS
0962F_WORKBENCH_PRESET_LIBRARY_VISIBLE_READONLY_APPLY_OR_HOLD_GATE=PASS
UI_PATCH_CANDIDATE_CREATED=true
UI_PATCH_APPLIED=false
VISIBLE_READONLY_APPLY_PERFORMED=false
VISIBLE_UI_APPLY_PERFORMED=false
TARGET_FILE=frontend/workbench/index.html
INSERT_AFTER=article[data-card="packageCheck"]
INSERT_BEFORE=div.extra-toggle
COMPONENT_DATA_CARD=presetLibraryReadonly
APPLY_ALLOWED_NEXT=true
APPLY_ALLOWED_NOW=false
INDEX_HTML_MODIFIED=false
FRONTEND_WORKBENCH_INDEX_MODIFIED=false
FRONTEND_RUNTIME_MODIFIED=false
ROUTE_CREATED=false
IMPORT_CREATED=false
BACKEND_MODIFIED=false
ENDPOINT_CREATED=false
PROVIDER_CALLED=false
MEMORY_STORE_WRITTEN=false
REGISTRY_STORE_WRITTEN=false
0962D_ZIP_ENTRY_COUNT=9
0962D_SHA256=d45858484a9da9e21533f1c6da5bf53429ba1816619ea97e491cf64c97fe20f0
0962E_ZIP_ENTRY_COUNT=10
0962E_SHA256=afdd2d6b1fe45c56f09fa6ff4db83230f3c3c8093932008511a7d51c8baceb36
0962F_ZIP_ENTRY_COUNT=11
0962F_SHA256=60ec0dbee9dce0a5aa17824d4b36f0c536fe9dbbdba0a9b73c9bb8b9375b806b
ZIP_PATHS_USE_FORWARD_SLASH=true
TEMP_ISOLATED_REVIEW_TREE_PASS=true
NEXT_STAGE=0963A_WORKBENCH_PRESET_LIBRARY_VISIBLE_READONLY_APPLY
NEXT_STAGE_REQUIRES_EXPLICIT_DECISION=true
```

## Safety Boundary

Do not archive or upload:

- `.env`
- token / secret / API key
- Feishu token or raw records
- real student private data
- provider raw prompt / response
- formal export payload containing sensitive data
