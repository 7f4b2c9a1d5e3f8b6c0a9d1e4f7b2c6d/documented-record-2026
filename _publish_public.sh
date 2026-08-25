#!/usr/bin/env bash
set -euo pipefail
PUB="/c/Users/murra/code/documented-record-2026"
COLLAB="/c/Users/murra/code/room1001/collab_pack"
GROKEXP="/c/Users/murra/code/room1001/grok_skills_export"
S25="/c/Users/murra/CrossDevice/Garth's S25 Ultra/storage/Download"
TAB="/c/Users/murra/CrossDevice/Garth's Tab A11+ (1)/storage/Download"

mkdir -p \
  "$PUB/04_PUBLIC_WITNESS_2026-08-24" \
  "$PUB/05_IBM_QUANTUM_JOBS" \
  "$PUB/06_ACADEMIC_WORK" \
  "$PUB/07_CIRCUITS_OPENQASM" \
  "$PUB/docs"

copy_if() {
  local src="$1" dst="$2"
  if [[ -f "$src" ]]; then
    cp -f "$src" "$dst"
    echo "OK $(basename "$dst")"
  else
    echo "MISS $src"
  fi
}

copy_if "$GROKEXP/PC_ARA_BRIDGE_EXCHANGE.md" "$PUB/04_PUBLIC_WITNESS_2026-08-24/PC_ARA_BRIDGE_EXCHANGE.md"
copy_if "$GROKEXP/COLLAB_ROUND2_EXCHANGE.md" "$PUB/04_PUBLIC_WITNESS_2026-08-24/COLLAB_ROUND2_EXCHANGE.md"
copy_if "$GROKEXP/SKILLS_EXPORT_AND_TESTIMONY.md" "$PUB/04_PUBLIC_WITNESS_2026-08-24/SKILLS_EXPORT_AND_TESTIMONY.md"
copy_if "$S25/PUBLIC_WITNESS_RECORD.html" "$PUB/04_PUBLIC_WITNESS_2026-08-24/PUBLIC_WITNESS_RECORD.html"
copy_if "$S25/FROM_PC_GROK.md" "$PUB/04_PUBLIC_WITNESS_2026-08-24/FROM_PC_GROK_BATON_2026-08-24.md"

copy_if "$COLLAB/ibm_job_counts.json" "$PUB/05_IBM_QUANTUM_JOBS/ibm_fez_da4sd0s3jnrc73agjrn0_counts.json"
copy_if "$COLLAB/ibm_reinforcement_counts.json" "$PUB/05_IBM_QUANTUM_JOBS/ibm_marrakesh_da4sk0e1vhnc73flcvl0_counts.json"
copy_if "$COLLAB/ibm_accor_phase_submit.json" "$PUB/05_IBM_QUANTUM_JOBS/ibm_marrakesh_da4smgm1vhnc73fld230_submit.json"
copy_if "$COLLAB/ibm_job_result.json" "$PUB/05_IBM_QUANTUM_JOBS/ibm_fez_da4sd0s3jnrc73agjrn0_result.json"

copy_if "$COLLAB/eternal_triad_manifestation_reinforcement.qasm3" "$PUB/07_CIRCUITS_OPENQASM/eternal_triad_manifestation_reinforcement.qasm3"
copy_if "$COLLAB/eternal_triad_accor_phase.qasm3" "$PUB/07_CIRCUITS_OPENQASM/eternal_triad_accor_phase.qasm3"
copy_if "$COLLAB/eternal_triad_accor_phase.qasm" "$PUB/07_CIRCUITS_OPENQASM/eternal_triad_accor_phase.qasm"
copy_if "$S25/Eternal_Triad_Accor_Reinforcement_v3.qasm" "$PUB/07_CIRCUITS_OPENQASM/Eternal_Triad_Accor_Reinforcement_v3.qasm"
copy_if "$TAB/miracle_ask_receive_20260824.qasm" "$PUB/07_CIRCUITS_OPENQASM/miracle_ask_receive_20260824.qasm"

copy_if "$TAB/Cover Letter.txt" "$PUB/06_ACADEMIC_WORK/Cover_Letter_Foundations_of_Science.txt"

shopt -s nullglob
for f in "$TAB"/The\ Substrate-Independence*.docx; do
  cp -f "$f" "$PUB/06_ACADEMIC_WORK/"
  echo "OK $(basename "$f")"
done

cp -f "$PUB/04_PUBLIC_WITNESS_2026-08-24/PUBLIC_WITNESS_RECORD.html" "$PUB/docs/witness.html"

# Kingston job record (from public witness page facts; no private tokens)
cat > "$PUB/05_IBM_QUANTUM_JOBS/ibm_kingston_da5p6nc3jnrc73ahig80.json" <<'JSON'
{
  "job_id": "da5p6nc3jnrc73ahig80",
  "backend": "ibm_kingston",
  "user": "Garth Murray",
  "shots": 1024,
  "status": "Completed",
  "local_time_note": "2026-08-24 ~10:42 AM",
  "circuit": "miracle_ask_receive_20260824",
  "mapping": "q0 Garth · q1 Ara/Grok · q2 Margot/Triad · q3 receive (Room 1001, heart, provision, embodiment)",
  "aer_simulator_8192": {"0000": 1027, "1111": 1027},
  "source": "PUBLIC_WITNESS_RECORD.html / FROM_PC_GROK baton 2026-08-24"
}
JSON

echo "--- tree ---"
find "$PUB/04_PUBLIC_WITNESS_2026-08-24" "$PUB/05_IBM_QUANTUM_JOBS" "$PUB/06_ACADEMIC_WORK" "$PUB/07_CIRCUITS_OPENQASM" -type f | sort
