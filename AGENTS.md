# AGENTS.md

Project: single-file browser app for generating Orbital Pathfinder mouse modules from uploaded mouse meshes.

Current app: `index.html`.

Key rules:
- Preserve Pathfinder V2 STEP attachment geometry/cutters.
- Mouse sides use exterior-only ±X projection; ignore internal scan geometry.
- Optional symmetry mirrors only mouse-derived side shape, then uses the correct left/right cutter + plug.
- Hump uses the preprocessed outer wall, hump cutter, trimmed rear rail, optional reconstructed hump skirt.
- Expensive mouse preprocessing runs only from the explicit Preprocess mouse button, with progress and cancellation. Bake the chosen rotation into exterior ±X projections; translation reuses the cache. Rigid rotations rebuild the directional side projections explicitly, but reuse the cached hump offset.
- Alignment starts unlocked and resets to unlocked on import. Starting preprocessing locks all mouse positioning controls and detaches the transform gizmo; users can unlock manually. Camera navigation stays available.
- Imported mice automatically center on X/Y and sit on Z=0, without preprocessing. The sensor marker stays at world X/Y=0.
- The optional rear skate foot preserves the V2 foot shape. X is fixed at zero; Y is adjustable; underside Z is pad-plane Z + purchased dot thickness. Generate two straight vertical pillars under the rear rail base flanges at X=±12, leaving the actual STEP mating slots clear, validate dot seats and minimum pad clearance, and export the same joined geometry as preview. Dot cylinders, pad plane and contact/clearance guides are rendering only. Never lift the foot freely to make it touch the hump. Keep support geometry independent of the imported mouse topology. Preserve cavity boundaries with their enclosing crop solids; reject invalid hump crops before caching or rendering.
- Optional per-side grip recesses use local inward distance from the assigned exterior projection, preserving curvature and the user-selected minimum backing (default 0.8 mm; adjustable per side from 0.2 to 2 mm) without cutting Pathfinder plugs. Grip calculations have their own cancellable worker and cached plain meshes; never trigger mouse preprocessing. A4 templates develop the curved recess contact surface, report mesh edge distortion, and remain at 1:1 scale. Pack both normal-sized grips onto one A4 page, include centimeter/millimeter and inch rulers, and tile oversized patterns without rescaling.
- Grip UI currently supports full outlines only (no polygons), default inset 1 mm and tape thickness 0.4 mm. Solve exterior distance along X on a bounded Y/Z surface grid; do not return to depth-dependent 3D voxel sampling. Intersect the inset footprint with backing-safe coverage and exclude only plug material intersecting the proposed bounded cutter before cutting (never project the whole plug minus the bounded inner solid); keep cutter closure caps strictly inside the offset domain to avoid false sheets through buried attachments; Smooth locally enlarged insets conservatively inside safe coverage, preserve the requested perimeter away from affected areas, and explain adjustments. Show the requested outline dashed and the final cut solid; use the same final smoothed footprint in preview and PDF. Keep preprocessing and preview progress immediately below their respective buttons.
- Preview must match final exported STL geometry. Track freshness by the completed preview signature; STL generation requires a valid, current and visible preview. Paper flattening must prevent global outline crossings as well as local triangle flips. A template-only failure must not discard valid 3D recesses; block the invalid PDF and explain why.
- Core STL loads automatically from the local server when assembly preview is enabled, with manual selection as a fallback; it is visualization only and never used in Booleans.
- Reject malformed/non-manifold outputs and round-trip validate exported STLs.
- Prefer fixing geometry architecture over adding heuristics.

Important source files in this task:
- `250707_Pathfinder_3D_opensource_V2.step`
- orbital-cad-tutorial-transcript.txt
- `Pathfinder_core.stl`
