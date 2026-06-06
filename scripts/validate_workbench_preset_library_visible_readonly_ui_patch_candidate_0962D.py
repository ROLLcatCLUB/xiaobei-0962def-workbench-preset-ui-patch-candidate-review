import argparse, json, zipfile
from pathlib import Path

CODE='0962D'
TITLE='WORKBENCH_PRESET_LIBRARY_VISIBLE_READONLY_UI_PATCH_CANDIDATE'
SLUG='workbench_preset_library_visible_readonly_ui_patch_candidate_0962D'
EXPECTED_STATUS='PASS'
PREFIX=f"{CODE}_{TITLE}_"
MARKER='ALL_0962D_WORKBENCH_PRESET_LIBRARY_VISIBLE_READONLY_UI_PATCH_CANDIDATE_CHECKS_OK'
FALSE_KEYS=['visible_readonly_apply_performed', 'ui_patch_applied', 'visible_ui_apply_performed', 'real_visible_preview_created', 'real_workbench_binding_created', 'workbench_binding_store_written', 'index_html_modified', 'frontend_workbench_index_modified', 'frontend_runtime_modified', 'frontend_modified', 'backend_modified', 'runtime_modified', 'endpoint_created', 'route_created', 'import_created', 'server_modified', 'component_grid_behavior_changed', 'real_registry_entry_created', 'registry_store_written', 'preset_library_store_written', 'provider_called', 'retrieval_enabled', 'provider_context_injection', 'memory_store_written', 'memory_read', 'memory_write', 'active_preset_scheme_created', 'published_preset_scheme_created', 'agent_published', 'agent_activated', 'ordinary_teacher_activated', 'admin_publish_performed', 'admin_activation_performed']

def load_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8-sig"))

def find_external(root, explicit):
    if explicit:
        return Path(explicit)
    reports = root / "reports" / PREFIX.rstrip("_")
    if reports.exists():
        return reports
    ext_root = root.parent / "xiaobei-core-external-reports"
    matches = sorted(ext_root.glob(PREFIX + "*")) if ext_root.exists() else []
    if matches:
        return matches[-1]
    raise SystemExit(f"external report dir missing for {PREFIX}")

def assert_false_flags(obj, label):
    bad=[k for k in FALSE_KEYS if obj.get(k) is not False]
    if bad:
        raise AssertionError(f"{label} forbidden flags not false: {bad}")

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--root", default="."); ap.add_argument("--external-dir", default=None); args=ap.parse_args()
    root=Path(args.root).resolve(); external=find_external(root,args.external_dir).resolve()
    contract=load_json(root/"docs/foundation"/f"{SLUG}.json"); result=load_json(external/f"{SLUG}_result.json"); checklist=load_json(external/f"{SLUG}_checklist.json"); manifest=load_json(external/f"{SLUG}_manifest.json")
    if contract.get("final_status") != EXPECTED_STATUS or result.get("final_status") != EXPECTED_STATUS: raise AssertionError("final_status mismatch")
    for label,obj in [("contract",contract),("result",result),("checklist",checklist)]: assert_false_flags(obj,label)
    candidate=load_json(root/"outputs/workbench_preset_library_visible_apply_0962D/ui_patch_candidate_0962D.json")
    if candidate.get("component_data_card") != "presetLibraryReadonly" or candidate.get("ui_patch_created") is not True:
        raise AssertionError("patch candidate missing")
    if candidate.get("ui_patch_applied") is not False or candidate.get("index_html_modified") is not False:
        raise AssertionError("candidate applied or index modified")
    html=(root/"outputs/workbench_preset_library_visible_apply_0962D/ui_patch_candidate_preview_0962D.html").read_text(encoding="utf-8-sig")
    for snippet in ['data-card="presetLibraryReadonly"','data-preset-library-readonly="0962D"','????']:
        if snippet not in html: raise AssertionError(f"html missing {snippet}")
    if '<script' in html.lower() or 'fetch(' in html: raise AssertionError("html contains executable/network code")
    if CODE in ["0962E","0962F"]:
        smoke=load_json(root/"outputs/workbench_preset_library_visible_apply_0962E/ui_patch_candidate_smoke_0962E.json")
        checks=smoke.get("checks",{})
        if not checks or any(v is not True for v in checks.values()): raise AssertionError("smoke checks not all true")
        assert_false_flags(smoke,"smoke")
    if CODE == "0962F":
        gate=load_json(root/"outputs/workbench_preset_library_visible_apply_0962F/apply_or_hold_gate_0962F.json")
        if gate.get("apply_allowed_next") is not True or gate.get("apply_allowed_now") is not False: raise AssertionError("gate decision mismatch")
        assert_false_flags(gate,"apply_gate")
    entries=manifest.get("zip_entries",[])
    if not entries: raise AssertionError("manifest zip_entries empty")
    if [n for n in entries if chr(92) in n or n.startswith("/") or ".." in Path(n).parts]: raise AssertionError("manifest contains unclean zip paths")
    zip_path=external/manifest.get("zip_file",f"{SLUG}_review_package.zip")
    if zip_path.exists():
        with zipfile.ZipFile(zip_path,"r") as zf: names=zf.namelist()
        if [n for n in names if chr(92) in n or n.startswith("/") or ".." in Path(n).parts]: raise AssertionError("zip contains unclean paths")
        if sorted(names)!=sorted(entries): raise AssertionError("zip/manifest mismatch")
    else:
        for entry in entries:
            if not (root/entry).exists(): raise AssertionError(f"zip missing and extracted entry missing: {entry}")
    print(MARKER)

if __name__=="__main__": main()
