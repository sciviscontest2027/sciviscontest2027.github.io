#!/usr/bin/env python3
"""One-off generator for the SciVis Contest 2027 static site.
Writes plain HTML pages that share the same nav/footer. No runtime dependencies."""
import os, shutil

OUT = os.path.dirname(os.path.abspath(__file__))
SRC_IMG = os.path.join(os.path.dirname(OUT), "images")

NAV = [
    ("index.html", "Home"),
    ("data.html", "Data"),
    ("tasks.html", "Tasks"),
    ("submissions.html", "Submissions"),
    ("archive.html", "Archive"),
    ("acknowledgements.html", "Acknowledgements"),
    ("pastcontests.html", "Past SciVis Contests"),
    ("faqs.html", "FAQs"),
]

def page(filename, title, body, desc="IEEE SciVis Contest 2027: visual analysis of additively manufactured lattice structures"):
    items = []
    for f, t in NAV:
        cls = ' class="active"' if f == filename else ""
        cur = ' aria-current="page"' if f == filename else ""
        items.append(f'        <li{cls}><a href="{f}"{cur}>{t}</a></li>')
    items = "\n".join(items)
    full_title = "IEEE SciVis Contest 2027" if filename == "index.html" else f"{title} | IEEE SciVis Contest 2027"
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{full_title}</title>
  <meta name="description" content="{desc}">
  <link rel="icon" type="image/png" href="images/logo.png">
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <header class="site-header">
    <div class="wrap nav-wrap">
      <a class="brand" href="index.html">
        <img src="images/logo.png" alt="" width="44" height="44">
        <span>SciVis Contest 2027</span>
      </a>
      <input type="checkbox" id="nav-toggle" class="nav-toggle" aria-label="Toggle navigation">
      <label for="nav-toggle" class="nav-burger"><span></span><span></span><span></span></label>
      <nav class="site-nav" aria-label="Main">
        <ul>
{items}
        </ul>
      </nav>
    </div>
  </header>

  <main>
{body}
  </main>

  <footer class="site-footer">
    <div class="wrap">
      <p>IEEE SciVis Contest 2027 &nbsp;|&nbsp; Co-organized with <a href="https://ieeevis.org">IEEE VIS</a> &nbsp;|&nbsp; Created at Lawrence Livermore National Laboratory &nbsp;|&nbsp; Questions: see <a href="acknowledgements.html">Organizers</a></p>
    </div>
  </footer>
</body>
</html>
"""

# ---------------------------------------------------------------- HOME
HOME = """
    <section class="hero">
      <div class="wrap hero-grid">
        <div class="hero-text">
          <p class="hero-kicker">IEEE VIS 2027</p>
          <h1>2027 IEEE SciVis Contest</h1>
          <p class="hero-sub">Micron-scale defects. Large-scale consequences.</p>
          <p class="hero-lead">Tiny defects hide inside 3D-printed metal lattices, and X-ray CT captures all of them, buried in gigabytes of volume data. This year's challenge: design the visualization that makes those flaws jump out, or build an autonomous AI agent that hunts them down and tells the story itself. Two tracks, one goal: show a materials scientist what went wrong, and where.</p>
          <p class="hero-actions">
            <a class="btn btn-primary" href="tasks.html">Read the tasks</a>
            <a class="btn btn-secondary" href="data.html">Get the data</a>
          </p>
        </div>
        <div class="hero-logo">
          <img src="images/logo.png" alt="2027 IEEE SciVis Contest logo: a laser melting a layer of metal powder on a build plate">
        </div>
      </div>
    </section>

    <section class="wrap section">
      <div class="prose">
        <h2>What is the SciVis Contest?</h2>
        <p>Welcome to the 2027 IEEE SciVis Contest, held annually as part of the <a href="https://ieeevis.org">IEEE VIS</a> conference. The 2027 contest, created in collaboration with the Advanced Materials Process Science Group at Lawrence Livermore National Laboratory (LLNL), focuses on the <strong>visual analysis of X-ray computed tomography (CT) scans of metal lattice structures produced by laser powder-bed fusion</strong>. The data are nine 9 × 9 × 9 octet-truss lattices printed at LLNL with intentionally missing struts; like every printed part, they also contain unintended defects. A lattice relies on thousands of thin struts, which makes it unusually sensitive to such defects, and finding them is what this contest asks you to do.</p>
        <p>The contest has <strong>two tasks</strong> at two scales of the same data (the individual strut and the entire part) and <strong>two tracks</strong> that differ in <em>who</em> creates the solution: a human visualization designer, or a fully autonomous agentic AI system.</p>
      </div>

      <table class="facts">
        <tbody>
          <tr><th scope="row">Domain</th><td>Additive manufacturing, non-destructive evaluation (NDE), materials science</td></tr>
          <tr><th scope="row">Data</th><td>X-ray CT volumes, as-designed STL meshes, and a nominal node/strut graph for nine 9 × 9 × 9 octet lattices</td></tr>
          <tr><th scope="row">Tasks</th><td><a href="tasks.html#task1">Task 1: Strut-level analysis</a> &nbsp;·&nbsp; <a href="tasks.html#task2">Task 2: Part-level analysis</a></td></tr>
          <tr><th scope="row">Tracks</th><td><a href="tasks.html#track-vis">Visualization Design Track</a> &nbsp;·&nbsp; <a href="tasks.html#track-agent">Agentic AI Track</a></td></tr>
          <tr><th scope="row">Submission</th><td>Report (3–4 pages, VGTC format) + video (≤ 10 min); Agentic AI Track additionally submits a ZIP of defect CSV files</td></tr>
          <tr><th scope="row">Prize</th><td>$1,000 cash prize for the top entry, sponsored by <a href="https://www.visoar.com/">ViSOAR</a></td></tr>
        </tbody>
      </table>
    </section>

    <section class="wrap section">
      <div class="features">
        <div class="feature">
          <h3>Two scales, one dataset</h3>
          <p>Task 1 looks at a single strut: is it as designed, and if not, what is wrong with it? Task 2 looks at the whole 20,000-strut part: where are the defects, do they cluster, and how do nine specimens compare?</p>
        </div>
        <div class="feature">
          <h3>Real parts, real consequences</h3>
          <p>The specimens are stainless-steel 316L octet lattices printed by laser powder-bed fusion with 0 %, 0.5 %, or 1 % of struts removed from the design (three specimens at each level; see the <a href="data.html#voxel-size">specimen table</a>). The as-built parts also contain defects nobody planned.</p>
        </div>
        <div class="feature">
          <h3>Human or AI agent</h3>
          <p>Enter the Visualization Design Track with any tools you choose, or the Agentic AI Track, where an autonomous system must find the missing struts and build the visualization with no human intervention after launch.</p>
        </div>
        <div class="feature">
          <h3>Win a cash prize</h3>
          <p>Submissions are evaluated by the contest jury on criteria such as usability, creativity, and innovation. The top entry will be awarded a $1,000 cash prize, generously sponsored by <a href="https://www.visoar.com/">ViSOAR</a>.</p>
        </div>
      </div>
    </section>

    <section class="wrap section" id="dates">
      <div class="prose">
        <h2>Important dates</h2>
      </div>
      <table class="dates">
        <tbody>
          <tr><td>November 9 2026</td><td>Official announcement at IEEE VIS 2026</td></tr>
          <tr class="deadline"><td>July 31, 2027 (23:59 AoE)</td><td>Submission deadline</td></tr>
          <tr><td>Approx. September 2027</td><td>Notification of shortlisted entries</td></tr>
          <tr><td>October/November 2027</td><td>Presentations by shortlisted teams at IEEE VIS 2027; winners announced</td></tr>
        </tbody>
      </table>
      <div class="prose">
        <p>On this website you can find information on the provided data, the visualization tasks, and the submission process. If you have any questions, feel free to contact the contest chairs listed under <a href="acknowledgements.html">Acknowledgements</a>.</p>
      </div>
    </section>

    <section class="wrap">
      <p class="release">LLNL-WEB-2025432. This work was performed under the auspices of the U.S. Department of Energy by Lawrence Livermore National Laboratory under contract DE-AC52-07NA27344. Lawrence Livermore National Security, LLC</p>
    </section>
"""

# ---------------------------------------------------------------- DATA
DATA = """
    <section class="page-title"><div class="wrap"><h1>Data</h1><p>Background on the specimens, and the files you will receive for each of the nine lattices.</p></div></section>
    <div class="wrap page-grid">
      <aside class="toc" aria-label="On this page">
        <p>On this page</p>
        <ol>
          <li><a href="#background">Background</a>
            <ol>
              <li><a href="#lpbf">Laser powder-bed fusion</a></li>
              <li><a href="#lattices">Lattices and the octet truss</a></li>
              <li><a href="#ct">Why X-ray CT</a></li>
              <li><a href="#prior-work">Strut-level visualization</a></li>
            </ol>
          </li>
          <li><a href="#dataset">The data</a>
            <ol>
              <li><a href="#specimens">Specimens</a></li>
              <li><a href="#files">Files per specimen</a></li>
              <li><a href="#voxel-size">CT voxel sizes</a></li>
              <li><a href="#build-direction">Build direction</a></li>
              <li><a href="#access">Access</a></li>
              <li><a href="#ground-truth">Held-out ground truth</a></li>
            </ol>
          </li>
        </ol>
      </aside>
      <article class="prose">
        <h2 id="background">Background</h2>

        <h3 id="lpbf">Laser powder-bed fusion</h3>
        <p>Laser powder-bed fusion (LPBF) is an additive manufacturing (AM) process for metals. A thin layer of metal powder (typically 20–60 µm) is spread across a build plate, a laser selectively melts one cross-section of the part, the platform lowers by one layer, and the cycle repeats thousands of times. Building layer by layer makes internal channels and lattice geometries possible that subtractive machining cannot produce.</p>
        <p>That freedom comes at a price. LPBF is sensitive to laser power, scan speed, layer thickness, build orientation, and local thermal history. Variation in these conditions produces porosity, lack of fusion, dimensional error, surface roughness, and adhered, partially melted powder (<em>dross</em>). Thin, overhanging, or poorly supported features such as lattice struts are particularly vulnerable.</p>

        <h3 id="lattices">Why lattice structures, and why the octet truss</h3>
        <p>Lattice structures are periodic networks of slender <em>struts</em> joined at <em>nodes</em>. By tuning the unit-cell topology, strut diameter, and cell size, engineers can tailor stiffness, strength, energy absorption, thermal transport, and mass independently of one another. This is why lattices appear in lightweight aerospace brackets, orthopedic implants that encourage bone in-growth, heat exchangers, and impact-mitigating structures.</p>
        <figure>
          <img src="images/octet_truss.png" alt="Octet-truss unit cell rendered as struts, with the underlying spatial graph (nodes and edges) overlaid." style="max-width:min(420px, 100%)">
          <figcaption><strong>Figure 1.</strong> An octet-truss unit cell. The gray cylinders are struts; the orange overlay is the nominal spatial graph with nodes (white) and edges. Every strut in the lattice is one edge of this graph. Image credit: adapted from Miao et al. [1]. © 2025 IEEE. Used with permission.</figcaption>
        </figure>
        <p>The <strong>octet truss</strong> (Figure 1) is one of the most widely used unit cells. It is built from a regular octahedron surrounded by eight tetrahedra, giving a stretch-dominated structure in which struts carry load primarily in tension and compression rather than bending. This yields a near-optimal strength-to-weight ratio and nearly isotropic mechanical behavior. Just as important for inspection, an octet lattice is highly regular: every unit cell is nominally identical, every strut has one of a small number of orientations, and the complete part can be described compactly as a <em>spatial graph</em> of nodes and edges. That regularity turns deviations from the expected pattern into strong indicators of manufacturing defects.</p>
        <figure class="wide">
          <img src="images/pic_octet.jpg" alt="Photograph of an LPBF-printed octet lattice with two magnified regions; one magnified region highlights a broken strut.">
          <figcaption><strong>Figure 2.</strong> A printed octet lattice. The magnified insets show the rough, powder-coated strut surfaces that are typical of LPBF, and a broken strut (left). Only struts on the exterior can be inspected visually; the thousands of struts in the interior are hidden. Image credit: adapted from Miao et al. [1]. © 2025 IEEE. Used with permission.</figcaption>
        </figure>
        <p>In a lattice, a single defective strut can matter. A missing, broken, or severely thinned strut removes a load path, and several defective struts in the same region can create a local weak zone that dominates the failure behavior of the whole part. For critical applications, the manufacturer therefore needs to know not just <em>whether</em> the part has defects but <em>how many</em>, <em>of which kind</em>, <em>where</em>, and <em>whether they cluster</em>.</p>

        <h3 id="ct">Why X-ray CT</h3>
        <p>A lattice cannot be inspected from the outside (Figure 2). X-ray computed tomography (CT) is the standard non-destructive technique for looking inside: the specimen is rotated in an X-ray beam, hundreds to thousands of radiographic projections are acquired, and a reconstruction algorithm produces a three-dimensional array of voxels whose intensity reflects X-ray attenuation. Dense metal appears bright, air appears dark, and the manufactured lattice can be separated from the background by segmentation.</p>

        <h3 id="prior-work">What has been done: strut-level visualization</h3>
        <p><em>LatticeAnalytics</em> (Miao et al., IEEE TVCG 2025 [1]) demonstrates a strut-centric inspection pipeline for mostly intact struts with problematic surfaces or shapes, and participants are welcome to build on its ideas. It also leaves much open: it relies on a manual VR alignment step, its encodings target roughness and bending rather than missing or disconnected struts, and it does not address the <em>part-level</em> questions at all (where defects occur, whether they cluster, how they relate to orientation and build height, and how lattices compare). Those gaps are the focus of this contest.</p>

        <h2 id="dataset">The data</h2>
        <p>The contest uses LLNL's <strong>Missing Struts</strong> dataset, which was created to develop inspection techniques for lattice defects [2]. It includes real CT scans of real printed parts.</p>

        <h3 id="specimens">Specimens</h3>
        <p>Nine 9 × 9 × 9 octet-truss lattice cubes were printed in stainless steel 316L by laser powder-bed fusion. The design specifications are:</p>
        <table>
          <thead><tr><th>Property</th><th>Design value</th></tr></thead>
          <tbody>
            <tr><td>Unit-cell topology</td><td>Octet truss</td></tr>
            <tr><td>Lattice size</td><td>9 × 9 × 9 unit cells</td></tr>
            <tr><td>Unit-cell edge length</td><td>4.56 mm</td></tr>
            <tr><td>Designed relative density</td><td>10 %</td></tr>
            <tr><td>Designed strut diameter</td><td>350 µm</td></tr>
            <tr><td>Material</td><td>Stainless steel 316L</td></tr>
            <tr><td>Process</td><td>Laser powder-bed fusion</td></tr>
            <tr><td>Nominal missing-strut fraction</td><td>0 %, 0.5 %, or 1 % of struts, depending on the specimen (three specimens per level)</td></tr>
          </tbody>
        </table>
        <p>Struts were removed from the design files at random before printing, at the nominal percentages above, so that the same inspection method can be tested against known defect fractions. Note that the as-built parts also contain defects that were <em>not</em> designed in: measured missing-strut percentages can exceed the nominal value, and disconnected or broken struts are commonly observed [2].</p>

        <h3 id="files">Files per specimen</h3>
        <p>Each specimen is delivered as a folder containing a CT volume and a nominal graph. The STL files describe the meshes used for printing; each printing mesh is shared by the three specimens of the same nominal fraction:</p>
        <table>
          <thead><tr><th>File</th><th>Format</th><th>Description</th></tr></thead>
          <tbody>
            <tr><td>CT volume</td><td>Stack of <code>.tif</code> slices</td><td>Reconstructed X-ray CT data, one stack per specimen (e.g., <code>210125_Brian_Tran_strut_lattice_01 1 Slices</code>). Grayscale intensity is proportional to X-ray attenuation. Slices are ordered along the build (z) direction. Voxel sizes are listed <a href="#voxel-size">below</a>.</td></tr>
            <tr><td>Printing meshes</td><td><code>.stl</code></td><td><code>0.stl</code> describes the complete lattice with no intentionally removed struts. The <code>0.5.stl</code> and <code>1.stl</code> meshes were used to print specimens with 0.5 % and 1 % of struts intentionally removed, respectively; those struts are already absent from these meshes.</td></tr>
            <tr><td>Nominal spatial graph</td><td><code>.json</code></td><td>Node positions and edge (strut) lists describing the lattice topology as designed.</td></tr>
          </tbody>
        </table>
        <aside class="note">
          <p><strong>Reference for missing-strut detection.</strong> If you choose to use an STL reference, use <code>0.stl</code> as the complete-lattice reference for any of the nine specimens. The <code>0.5.stl</code> and <code>1.stl</code> files should not be used to detect missing struts: they were used to print the intentionally embedded defects and already omit the struts to be detected. Using an STL file is optional.</p>
          <p><strong>Registration note.</strong> The STL mesh is <strong>not</strong> registered to the TIF stack or the JSON graph. Registration between the design and the scan is a problem in its own right, and solving it well is a valid contribution. For teams that prefer to start with analysis, the JSON graph of one specimen (<code>210127_Brian_Tran_strut_lattices_0point5dash1 1 Slices.json</code>) is already aligned with the TIF stack of the same name. Participants may use this specimen to develop their pipeline.</p>
        </aside>

        <h3 id="voxel-size">Specimens, dataset names, and CT voxel sizes</h3>
        <p>The table below maps each specimen to its dataset folder name, the mesh used to print it, and its CT voxel size. The printing-mesh column records how each specimen was manufactured; for missing-strut detection with an STL reference, use <code>0.stl</code> for every specimen. On this site, specimens are referred to by nominal missing-strut percentage and replicate number (<code>0.5-1</code> is the first replicate at 0.5 %, i.e., dataset <code>210127_Brian_Tran_strut_lattices_0point5dash1 1 Slices</code>). The CT volumes are stored as integer voxel grids without embedded physical units; use the voxel sizes to convert voxel indices and distances to physical units (e.g., when comparing measured strut diameters to the designed 350 µm). Note that the three 0 % specimens were scanned with slightly anisotropic voxels.</p>
        <table>
          <thead><tr><th>Specimen</th><th>Nominal missing struts</th><th>Dataset folder</th><th>Mesh used for printing</th><th>Voxel size [x, y, z] (µm)</th></tr></thead>
          <tbody>
            <tr><td><code>0-1</code></td><td>0 %</td><td><code>210125_Brian_Tran_strut_lattice_01 1 Slices</code></td><td><code>0.stl</code></td><td>[55.32, 58.41, 56.54]</td></tr>
            <tr><td><code>0-2</code></td><td>0 %</td><td><code>210125_Brian_Tran_strut_lattice_02 1 Slices</code></td><td><code>0.stl</code></td><td>[56.65, 58.22, 56.50]</td></tr>
            <tr><td><code>0-3</code></td><td>0 %</td><td><code>210125_Brian_Tran_strut_lattice_03 1 Slices</code></td><td><code>0.stl</code></td><td>[58.10, 58.10, 58.10]</td></tr>
            <tr><td><code>0.5-1</code></td><td>0.5 %</td><td><code>210127_Brian_Tran_strut_lattices_0point5dash1 1 Slices</code></td><td><code>0.5.stl</code></td><td>[58.09, 58.09, 58.09]</td></tr>
            <tr><td><code>0.5-2</code></td><td>0.5 %</td><td><code>210127_Brian_Tran_strut_lattices_0point5dash2 1 Slices</code></td><td><code>0.5.stl</code></td><td>[58.09, 58.09, 58.09]</td></tr>
            <tr><td><code>0.5-3</code></td><td>0.5 %</td><td><code>210127_Brian_Tran_strut_lattices_0point5dash3 1 Slices</code></td><td><code>0.5.stl</code></td><td>[58.09, 58.09, 58.09]</td></tr>
            <tr><td><code>1-1</code></td><td>1 %</td><td><code>210127_Brian_Tran_strut_lattices_1_1 1 Slices</code></td><td><code>1.stl</code></td><td>[58.09, 58.09, 58.09]</td></tr>
            <tr><td><code>1-2</code></td><td>1 %</td><td><code>210127_Brian_Tran_strut_lattices_1_2 1 Slices</code></td><td><code>1.stl</code></td><td>[58.09, 58.09, 58.09]</td></tr>
            <tr><td><code>1-3</code></td><td>1 %</td><td><code>210127_Brian_Tran_strut_lattices_1_3 1 Slices</code></td><td><code>1.stl</code></td><td>[58.09, 58.09, 58.09]</td></tr>
          </tbody>
        </table>
        <p>Each lattice is sandwiched between two solid plates, and the assembly was built with the plates standing <em>vertically</em> on the build platform, so the build direction runs parallel to the plates and along one edge of the lattice (Figure 3). "Bottom" and "top" in the sense of build height are therefore the lattice faces closest to and farthest from the build platform, not the faces touching the plates.</p>
        <figure>
          <img src="images/build_direction.png" alt="Side view of an octet lattice between two solid vertical plates, with an arrow labeled Build Direction pointing upward." style="max-width:min(460px, 100%)">
          <figcaption><strong>Figure 3.</strong> Build orientation of the specimens. The lattice (black) sits between two solid plates (gray). The build direction (arrow) is vertical and parallel to the plates; each printed layer is a horizontal cross-section of this view.</figcaption>
        </figure>
        <p>The build direction is the most important geometric reference in this contest, because strut quality in LPBF depends on a strut's angle to it and on its distance from the build platform. In the data, the build direction is the slice-stacking axis of the CT volume (z in the TIF stack). Measure build height, strut inclination, and orientation-dependent statistics relative to this axis.</p>

        <h3 id="access">Access</h3>
        <h4>Download CT data</h4>
        <p>Download the CT volumes as TIF stacks: <a href="https://gdo172.llnl.gov/data/tif_stacks.tar.gz">tif_stacks.tar.gz</a>.</p>

        <h4>Stream with OpenVisus</h4>
        <p>To stream the CT data directly with OpenVisus, use the dataset URLs below. Copy a link address into your OpenVisus client to load that specimen without downloading the full TIF archive.</p>
        <table>
          <thead><tr><th scope="col">Specimen</th><th scope="col">OpenVisus dataset URL</th></tr></thead>
          <tbody>
            <tr><th scope="row"><code>0-1</code></th><td><a href="https://olympus.sci.utah.edu/mod_visus?dataset=210125_Brian_Tran_strut_lattice_01_1_Slices">210125_Brian_Tran_strut_lattice_01_1_Slices</a></td></tr>
            <tr><th scope="row"><code>0-2</code></th><td><a href="https://olympus.sci.utah.edu/mod_visus?dataset=210125_Brian_Tran_strut_lattice_02_1_Slices">210125_Brian_Tran_strut_lattice_02_1_Slices</a></td></tr>
            <tr><th scope="row"><code>0-3</code></th><td><a href="https://olympus.sci.utah.edu/mod_visus?dataset=210125_Brian_Tran_strut_lattice_03_1_Slices">210125_Brian_Tran_strut_lattice_03_1_Slices</a></td></tr>
            <tr><th scope="row"><code>0.5-1</code></th><td><a href="https://olympus.sci.utah.edu/mod_visus?dataset=210127_Brian_Tran_strut_lattices_0point5dash1_1_Slices">210127_Brian_Tran_strut_lattices_0point5dash1_1_Slices</a></td></tr>
            <tr><th scope="row"><code>0.5-2</code></th><td><a href="https://olympus.sci.utah.edu/mod_visus?dataset=210127_Brian_Tran_strut_lattices_0point5dash2_1_Slices">210127_Brian_Tran_strut_lattices_0point5dash2_1_Slices</a></td></tr>
            <tr><th scope="row"><code>0.5-3</code></th><td><a href="https://olympus.sci.utah.edu/mod_visus?dataset=210127_Brian_Tran_strut_lattices_0point5dash3_1_Slices">210127_Brian_Tran_strut_lattices_0point5dash3_1_Slices</a></td></tr>
            <tr><th scope="row"><code>1-1</code></th><td><a href="https://olympus.sci.utah.edu/mod_visus?dataset=210127_Brian_Tran_strut_lattices_1_1_1_Slices">210127_Brian_Tran_strut_lattices_1_1_1_Slices</a></td></tr>
            <tr><th scope="row"><code>1-2</code></th><td><a href="https://olympus.sci.utah.edu/mod_visus?dataset=210127_Brian_Tran_strut_lattices_1_2_1_Slices">210127_Brian_Tran_strut_lattices_1_2_1_Slices</a></td></tr>
            <tr><th scope="row"><code>1-3</code></th><td><a href="https://olympus.sci.utah.edu/mod_visus?dataset=210127_Brian_Tran_strut_lattices_1_3_1_Slices">210127_Brian_Tran_strut_lattices_1_3_1_Slices</a></td></tr>
          </tbody>
        </table>

        <h3 id="ground-truth">Held-out ground truth</h3>
        <p>For the purpose of evaluating the Agentic AI Track, the organizers hold a curated list of the missing struts for every specimen: the struts that were intentionally omitted in the design, verified against the CT volume. This list is not released during the contest. After the contest, the full ground truth will be published together with the submissions so that the dataset can serve as a lasting benchmark.</p>

        <p class="refs-pointer">Numbered citations refer to the <a href="acknowledgements.html#references">reference list</a>.</p>
      </article>
    </div>
"""

# ---------------------------------------------------------------- TASKS
TASKS = """
    <section class="page-title"><div class="wrap"><h1>Tasks</h1><p>Two tasks at two scales of the same data, two tracks that differ in who builds the solution, and how the jury evaluates each.</p></div></section>
    <div class="wrap page-grid">
      <aside class="toc" aria-label="On this page">
        <p>On this page</p>
        <ol>
          <li><a href="#overview">1. Challenge overview</a></li>
          <li><a href="#task1">2. Task 1: Strut-level analysis</a>
            <ol>
              <li><a href="#strut-features">2.1 Strut-level features</a></li>
              <li><a href="#defect-classification">2.2 Defect classification</a></li>
              <li><a href="#strut-vis">2.3 Strut-level visualization</a></li>
            </ol>
          </li>
          <li><a href="#task2">3. Task 2: Part-level analysis</a>
            <ol>
              <li><a href="#designed-vs-built">3.1 Designed versus as-built part</a></li>
              <li><a href="#defect-statistics">3.2 Defect statistics</a></li>
              <li><a href="#defect-location">3.3 Where do defects occur?</a></li>
              <li><a href="#specimen-comparison">3.4 Comparison across specimens</a></li>
              <li><a href="#mechanical">3.5 Toward mechanical consequences</a></li>
              <li><a href="#part-vis">3.6 Part-level visualization</a></li>
            </ol>
          </li>
          <li><a href="#tracks">4. Tracks</a>
            <ol>
              <li><a href="#track-vis">4.1 Visualization Design Track</a></li>
              <li><a href="#track-agent">4.2 Agentic AI Track</a></li>
            </ol>
          </li>
          <li><a href="#evaluation">5. Evaluation</a>
            <ol>
              <li><a href="#eval-vis">5.1 Visualization Design Track</a></li>
              <li><a href="#eval-agent">5.2 Agentic AI Track</a></li>
            </ol>
          </li>
        </ol>
      </aside>
      <article class="prose">
        <h2 id="overview">1. Challenge overview</h2>
        <p>The overall goal is simple to state: <strong>help a materials scientist understand the quality of a printed lattice from its CT scan</strong>, both at the level of individual struts and at the level of the whole part, and do so across lattices with different defect fractions.</p>
        <p>Participants are not required to answer every question; a focused, well-executed treatment of a subset is preferable to a shallow treatment of everything. You are also encouraged to go beyond the listed questions if the data suggests something interesting.</p>

        <h2 id="task1">2. Task 1: Strut-level analysis</h2>
        <dl class="scale">
          <dt>Scale</dt><dd>One strut, or a small set of struts, at a time.</dd>
          <dt>Core question</dt><dd><em>Is this strut as designed, and if not, what is wrong with it?</em></dd>
        </dl>
        <p>The output of this task is a per-strut description: features, a defect classification, and a visual representation that lets an expert verify the classification quickly and confidently.</p>
        <p>Note that missing struts are the only defect that was <em>designed in</em>. The scans also contain broken, thinned, bent, and fused struts that nobody planned (see <a href="data.html">Data</a>), and Task 1 covers all of them: a strut that is present but defective is just as much a finding as one that is absent.</p>

        <h3 id="strut-features">2.1 Strut-level features</h3>
        <p>Compute and/or visualize, for every strut, features that describe how it deviates from its design. Suggested features include:</p>
        <ul>
          <li><strong>Dimensions.</strong> Length between nodes, mean/min/max diameter along the strut, and comparison to the designed 350 µm diameter and designed length.</li>
          <li><strong>Continuity.</strong> Whether material is present along the whole centerline; location and extent of any gap.</li>
          <li><strong>Thickness profile.</strong> Diameter as a function of position along the strut; thinning toward the middle is a typical precursor to breakage.</li>
          <li><strong>Cross-sectional shape.</strong> Deviation from a circle (e.g., ellipse aspect ratio, circularity), and whether the deviation has a consistent orientation (e.g., elongated along the build direction).</li>
          <li><strong>Straightness.</strong> Curvature or bow of the centerline relative to the straight nominal strut.</li>
          <li><strong>Surface.</strong> Roughness or adhered powder; excess material near nodes (dross).</li>
        </ul>

        <h3 id="defect-classification">2.2 Defect classification</h3>
        <p>Classify each strut as <strong>normal</strong>, <strong>missing</strong> (no material along the designed path), <strong>broken</strong> (material present at both ends but with at least one gap), <strong>thin</strong> (continuous but substantially under the designed diameter), or <strong>other</strong> (e.g., bent, dross, fused to a neighbor). Define your thresholds explicitly and show how sensitive the classification is to them. Because imaging artifacts can mimic defects, the classification should be <em>verifiable</em>: the expert must be able to look at a flagged strut and decide within seconds whether the flag is right.</p>

        <h3 id="strut-vis">2.3 Strut-level visualization</h3>
        <p>Design a visual representation of a single strut, and of a small set of struts side by side, that supports verification and comparison. This is where the visualization research question lives. Consider how your strut view communicates uncertainty from segmentation and registration, how it scales to browsing hundreds of flagged struts, and how it links to the part-level views of Task 2.</p>

        <h2 id="task2">3. Task 2: Part-level analysis</h2>
        <dl class="scale">
          <dt>Scale</dt><dd>The whole lattice, and the set of nine lattices.</dd>
          <dt>Core question</dt><dd><em>What is the overall quality of this part, where are its weaknesses, and why might they be there?</em></dd>
        </dl>
        <p>The output of this task is an assessment of the part, the kind of thing a materials scientist would put in an inspection report or show to a design team, backed by visualizations that make the spatial and statistical structure of the defects understandable. Part-level statistics should cover every defect category of Task 1, not only the designed-in missing struts.</p>

        <h3 id="designed-vs-built">3.1 Designed versus as-built part</h3>
        <ul>
          <li>Calculate the designed number of struts and nodes from the nominal graph (or the STL) for a 9 × 9 × 9 octet lattice, accounting for the struts that were intentionally removed.</li>
          <li>Measure actual unit-cell dimensions (cell pitch along each axis, overall part dimensions) from the CT data and compare them to the design; characterize shrinkage, warping, or anisotropy.</li>
          <li>Reconstruct the as-built part as a 3D model (surface or graph) and compare it to the STL design. A global deviation map is one approach; a graph-to-graph comparison is another.</li>
        </ul>

        <h3 id="defect-statistics">3.2 Defect statistics</h3>
        <ul>
          <li>Count defective struts by category and in total, as absolute numbers and as percentages of the designed strut count.</li>
          <li>Compare the measured missing-strut fraction to the nominal design fraction (0 %, 0.5 %, or 1 %; see the <a href="data.html#voxel-size">specimen table</a> for which dataset is which). Explain discrepancies.</li>
        </ul>

        <h3 id="defect-location">3.3 Where do defects occur?</h3>
        <ul>
          <li><strong>Build height.</strong> Stratify defects by distance from the build plate: near the plate, in the middle, near the top. Is there a trend? (LPBF thermal history and support conditions vary with height.)</li>
          <li><strong>Exterior versus bulk.</strong> Compare defect rates on the outer unit-cell shell to the interior.</li>
          <li><strong>Spatial pattern.</strong> Are defects clustered or randomly distributed? Use and visualize an appropriate spatial statistic (nearest-neighbor distances, Ripley's K, a null model of random strut removal) and show the evidence, not just a p-value.</li>
          <li><strong>Orientation.</strong> Group struts by orientation relative to the build direction (e.g., horizontal, inclined, vertical) and compare defect rates; in LPBF, horizontal and downward-facing features are the hardest to print.</li>
          <li><strong>Other factors.</strong> Node degree, distance from the part's edge, proximity to other defects, or anything else you find predictive.</li>
        </ul>

        <h3 id="specimen-comparison">3.4 Comparison across specimens</h3>
        <p>Apply the same pipeline to all nine lattices and compare them. Do the three nominal defect fractions separate cleanly in the measured data? Are the <em>unintended</em> defects (broken, thin, missing) similar across specimens, which would point to the process, or do they vary, which would point to the individual build? Design visualizations that support comparing nine parts at once.</p>

        <h3 id="mechanical">3.5 Toward mechanical consequences (advanced)</h3>
        <p>The materials scientist's hardest question is at what defect fraction the lattice strength is significantly affected. Participants may approach this with a simple structural model on the as-built graph (e.g., a truss or beam finite-element model with the measured defects removed), with published results on octet-lattice stiffness versus defect density, or with a visual analysis that connects defect clusters to plausible load paths. Any such analysis should be clear about its assumptions.</p>

        <h3 id="part-vis">3.6 Part-level visualization</h3>
        <p>The design challenge is to show a 20,000-strut lattice in a way that reveals a few hundred defective struts, their spatial distribution, and their relationship to build height, orientation, and the exterior, without the occlusion that defeats naive 3D rendering. Abstractions of the lattice (the spatial graph, unit-cell grids, per-layer or per-shell summaries, unrolled or projected layouts), focus-and-context techniques, small multiples across specimens, and linked strut-level detail views are all fair game. The visualizations should also work as static figures for presentations and data sharing.</p>

        <h2 id="tracks">4. Tracks</h2>
        <p>Every submission enters exactly one track. The tracks address the same tasks on the same data (Task 1 and Task 2, described above) but differ in <em>how</em> the solution is produced and in the research question they ask: one about visualization design, the other about autonomous AI.</p>
        <table class="tracks">
          <thead><tr><th></th><th class="col-vis">Visualization Design Track</th><th class="col-agent">Agentic AI Track</th></tr></thead>
          <tbody>
            <tr><th scope="row">Who creates the analysis/visualization</th><td>Humans, with any tools they choose</td><td>An autonomous agentic system, with no human intervention after launch</td></tr>
            <tr><th scope="row">Research question</th><td>What visual encodings, interactions, and analysis workflows best answer the domain scientist's questions?</td><td>Can an agentic system autonomously find the missing struts, characterize the other defects, and produce an effective system for the task?</td></tr>
            <tr><th scope="row">Primary evidence</th><td>Report, video, figures</td><td>Defect CSVs (missing struts scored against held-out ground truth), the generated visualization system, report, video</td></tr>
          </tbody>
        </table>

        <section class="track track-vis" id="track-vis">
          <p class="track-label">Track</p>
          <h3>4.1 Visualization Design Track</h3>
          <p class="track-tagline">Humans design the analysis and visualization, with any tools they choose.</p>
        <p>Strong submissions in this track typically:</p>
        <ul>
          <li>articulate the domain questions as concrete visualization tasks and show how each design decision serves them;</li>
          <li>demonstrate the system on the real data, with concrete findings (e.g., "defects in specimen X concentrate in the lowest two cell layers and are predominantly horizontal struts");</li>
          <li>address both the strut level and the part level, and the link between them;</li>
          <li>treat uncertainty and verification as first-class concerns;</li>
          <li>evaluate the approach, whether through a case study, expert feedback, or comparison with a baseline.</li>
        </ul>

        </section>

        <section class="track track-agent" id="track-agent">
          <p class="track-label">Track</p>
          <h3>4.2 Agentic AI Track</h3>
          <p class="track-tagline">An autonomous agentic AI system does the work, with no human intervention after launch.</p>
        <p>This track asks whether an autonomous agentic AI system can carry out the inspection end to end. The system is given the data and a task description and must, <strong>without human intervention after launch</strong>, (a) detect the missing struts in each specimen and report their locations in a machine-readable file, and (b) create a system or set of visualizations that addresses Tasks 1 and 2.</p>
        <p>For related work on agentic AI for visualization, see <em>Toward AI VIS Co-Scientists</em> <a href="acknowledgements.html#ref-ai-vis-co-scientists">[5]</a>, which presents a general, end-to-end agent harness for complex data visualization tasks.</p>

        <h4 id="autonomy">4.2.1 Autonomy requirements</h4>
        <ul>
          <li>Participants may design the agentic system in advance in any way they wish: choice of models, frameworks, tools (e.g., MCP servers, tool-use), skills, sub-agents, memory, prompts, and any software the agent can call. Development and testing on the contest data before the final run is allowed.</li>
          <li>Human-written code is permitted <em>inside tools the agent calls</em> (e.g., a segmentation library) but not as a step that a human executes between agent actions. The distinction we care about is: once the run starts, nobody touches it.</li>
          <li>Any model is allowed (local or API, open or closed). Report the models used, approximate compute, and cost.</li>
        </ul>

        <h4 id="csv">4.2.2 Required output: defect CSV</h4>
        <p>For <strong>each</strong> of the nine specimens, the agent must produce one CSV file listing the detected defective struts, each labeled with its defect type.</p>
        <p><strong>File naming.</strong> <code>&lt;specimen_folder_name&gt;.csv</code>, named exactly after the specimen folder.</p>
        <p><strong>Format.</strong> UTF-8, comma-separated, with a header row. Columns:</p>
        <table>
          <thead><tr><th>Column</th><th>Required</th><th>Description</th></tr></thead>
          <tbody>
            <tr><td><code>x</code></td><td><strong>mandatory</strong></td><td>Column index (voxels) of the strut center</td></tr>
            <tr><td><code>y</code></td><td><strong>mandatory</strong></td><td>Row index (voxels) of the strut center</td></tr>
            <tr><td><code>z</code></td><td><strong>mandatory</strong></td><td>Slice index (voxels) of the strut center</td></tr>
            <tr><td><code>strut_id</code></td><td>optional</td><td>Identifier of the strut in the nominal JSON graph (edge index), if the agent established the correspondence</td></tr>
            <tr><td><code>node_a</code>, <code>node_b</code></td><td>optional</td><td>Identifiers of the two end nodes in the nominal graph</td></tr>
            <tr><td><code>defect_type</code></td><td><strong>mandatory</strong></td><td>One of <code>missing</code>, <code>broken</code>, <code>thin</code>, or <code>other</code> (the categories of Task 1). Only <code>missing</code> rows enter the detection score (criterion (a) under <a href="#evaluation">Evaluation</a>); <code>broken</code>, <code>thin</code>, and <code>other</code> rows are not scored there and do not count as false positives, but the agent is expected to report them and to address those defects in its visualization output (criteria (b) and (c)). Rows with a missing or unrecognized label are ignored.</td></tr>
            <tr><td><code>confidence</code></td><td>optional</td><td>A value in [0, 1]</td></tr>
          </tbody>
        </table>
        <p><strong>What "strut center" means.</strong> The location of a missing strut is the <strong>midpoint between the two nodes that the strut would have connected</strong>, i.e., the center of the designed strut, expressed in the voxel coordinate convention of the CT volume (see <a href="data.html#build-direction">Data</a>). Because the strut itself is absent, the location must be inferred from the surrounding lattice (the positions of the two nodes, the pattern of neighboring struts, or the registered nominal graph). For <code>broken</code>, <code>thin</code>, and <code>other</code> rows, report the center of the as-designed strut in the same way.</p>
        <p><strong>Tolerance.</strong> A <code>missing</code> detection is counted as correct if its reported center is within <strong>20 voxels</strong> (Euclidean distance) of a ground-truth missing-strut center. Each ground-truth strut can be matched by at most one detection; each detection can match at most one ground-truth strut (one-to-one matching, nearest first).</p>
        <p>Example:</p>
<pre><code>x,y,z,strut_id,node_a,node_b,defect_type,confidence
1043.5,612.0,287.0,4518,1207,1340,missing,0.97
388.0,1290.5,1455.0,,,,missing,0.81
702.0,702.0,1810.0,9931,2611,2744,broken,0.66</code></pre>

        <h4 id="vis-system">4.2.3 Required output: visualization system</h4>
        <p>Beyond the CSVs, the agentic system must generate the visualization component of the submission: a dashboard, an application, a notebook, or a set of static figures that addresses Tasks 1 and 2 (strut-level verification and part-level assessment).</p>

        <h4 id="report-not-agent">4.2.4 What is not an agent output: the report</h4>
        <p>The autonomy requirement applies to the two outputs above and <strong>not</strong> to the report. The report is written by the participants after the final run and is a reflection <em>on</em> the agent rather than a product <em>of</em> it; the jury evaluates criterion (d) and the autonomy criterion below primarily from it. See <a href="submissions.html#include">What to include</a> for the required content.</p>
        </section>

        <h2 id="evaluation">5. Evaluation</h2>
        <p>A jury of visualization researchers, AI/ML experts, and materials scientists reviews all submissions. The two tracks are judged separately.</p>
        <p>The criteria below are also the structure we expect in the report: please address each criterion for your track explicitly, so that the jury can find the relevant evidence without having to infer it. A short subsection or paragraph per criterion is sufficient; criteria you deliberately did not pursue should be named as such with a one-line justification rather than left out.</p>

        <h3 class="h-track-vis" id="eval-vis">5.1 Visualization Design Track</h3>
        <table>
          <thead><tr><th>Criterion</th><th>What we look for</th></tr></thead>
          <tbody>
            <tr><td><strong>Task coverage and insight</strong></td><td>Are the strut-level and part-level questions addressed? Are there concrete findings about the data?</td></tr>
            <tr><td><strong>Visual encoding and interaction design</strong></td><td>Are the encodings appropriate, justified, and effective for the multi-scale problem? Is uncertainty communicated?</td></tr>
            <tr><td><strong>Analysis quality</strong></td><td>Are the measurements, classifications, and statistics sound? Are thresholds and assumptions explicit?</td></tr>
            <tr><td><strong>Scalability and generality</strong></td><td>Does the approach handle all nine specimens? Would it transfer to other lattices?</td></tr>
            <tr><td><strong>Reflection</strong></td><td>Case study, comparison with baselines, honest discussion of limitations.</td></tr>
            <tr><td><strong>Communication</strong></td><td>Clarity of report, video, and figures.</td></tr>
          </tbody>
        </table>

        <h3 class="h-track-agent" id="eval-agent">5.2 Agentic AI Track</h3>
        <table>
          <thead><tr><th>Criterion</th><th>What we look for</th></tr></thead>
          <tbody>
            <tr><td><strong>(a) Detection performance</strong></td><td>Recall, precision, and F1 of missing-strut detection on the randomly selected specimen, 20-voxel tolerance.</td></tr>
            <tr><td><strong>(b) Efficacy of visual encodings</strong></td><td>Quality and appropriateness of the strut-level and part-level visualizations the system generated.</td></tr>
            <tr><td><strong>(c) Overall visualization design and goal attainment</strong></td><td>Coherence and usability of the generated system; does it let a scientist answer Tasks 1 and 2?</td></tr>
            <tr><td><strong>(d) Agentic design and efficiency</strong></td><td>Quality of the agent architecture (tools, skills, sub-agents, planning, self-verification, error recovery); robustness; transparency; token, time, and compute cost per specimen.</td></tr>
            <tr><td><strong>Autonomy and transparency</strong></td><td>Credibility of the no-intervention protocol; completeness of the architecture description; reproducibility.</td></tr>
            <tr><td><strong>Communication</strong></td><td>Clarity of report and video.</td></tr>
          </tbody>
        </table>
      </article>
    </div>
"""

# ---------------------------------------------------------------- SUBMISSIONS
SUBMISSIONS = """
    <section class="page-title"><div class="wrap"><h1>Submissions</h1><p>What to include, how to submit through the Precision Conference System, and the key dates.</p></div></section>
    <div class="wrap page-grid">
      <aside class="toc" aria-label="On this page">
        <p>On this page</p>
        <ol>
          <li><a href="#include">What to include</a></li>
          <li><a href="#how">How to submit</a></li>
          <li><a href="#dates">Important dates</a></li>
        </ol>
      </aside>
      <article class="prose">
        <h2 id="include">What to include</h2>
        <p>All submissions, in both tracks, consist of:</p>
        <ol>
          <li><strong>Report (PDF).</strong> A 3–4 page manuscript in the <a href="https://tc.computer.org/vgtc/publications/conference/">VGTC conference format</a> (LaTeX and Word templates available), plus up to one additional page for references. Focus on methods, design rationale, and results; keep background and data description brief, since the readers know the data. Figures may be appended after the references. Maximum file size 50 MB. The report must state the track and list all authors, and it should address each of the <a href="tasks.html#evaluation">evaluation criteria</a> for its track. <br><br>For the Agentic AI Track, the report is a human-authored account of the agent (see <a href="tasks.html#report-not-agent">the track description</a>) and must cover: (i) the <strong>agent architecture</strong>: models, tools, skills, sub-agents, memory, planning and verification strategy, and the initial prompt(s); (ii) the <strong>autonomy protocol</strong> of the final run: how it was launched, how long it ran, and evidence that nobody intervened; (iii) <strong>failure modes</strong>: what went wrong during development, how the design mitigates it, and what still failed or was fragile in the final run; (iv) a <strong>self-assessment</strong> of the generated visualization system against Tasks 1 and 2, including what the team would have designed differently by hand; and (v) <strong>compute and cost</strong>: tokens, wall-clock time, hardware, and approximate monetary cost per specimen. Figures reproducing agent-generated visualizations are welcome and should be labeled as agent output; human-made figures (e.g., an architecture diagram) should be distinguishable from them.</li>
          <li><strong>Video.</strong> An MPEG, AVI, MP4, or QuickTime video of at most 10 minutes demonstrating the system, methods, or process in action. For the Agentic AI Track, we encourage including footage of the autonomous run.</li>
        </ol>
        <p>Agentic AI Track submissions additionally include:</p>
        <ol start="3">
          <li><strong>ZIP archive of defect CSVs.</strong> The nine per-specimen CSVs of the <a href="tasks.html#csv">CSV specification</a> in a single ZIP file. Optionally, the ZIP may also contain the initial prompt(s), the agent configuration, and run logs; these are helpful for verification but are not required.</li>
        </ol>
        <p>Individual and group submissions are both welcome. Please include the full author list at submission time.</p>

        <h2 id="how">How to submit</h2>
        <p>Submissions are made through the <a href="https://new.precisionconference.com">Precision Conference System</a>:</p>
        <ol>
          <li>Sign in or create an account.</li>
          <li>Open the <strong>Submissions</strong> tab.</li>
          <li>Under <strong>Make a new submission</strong>, select <strong>VGTC</strong> (Society), <strong>VIS 2027</strong> (Conference/Journal), and <strong>VIS 2027 SciVis Contest</strong> (Track).</li>
          <li>Upload the report, the video, and (Agentic AI Track) the ZIP archive, and indicate your track in the submission form.</li>
        </ol>
        <p>Top entries will be invited to present at the SciVis Contest session at IEEE VIS 2027, and the best submission may be invited to submit an extended version to <em>IEEE Computer Graphics and Applications</em>. The top entry receives a <strong>$1,000 cash prize</strong> sponsored by <a href="https://www.visoar.com/">ViSOAR</a>; any additional prizes will be announced on this website.</p>

      </article>
    </div>
"""

# ---------------------------------------------------------------- ARCHIVE
ARCHIVE = """
    <section class="page-title"><div class="wrap"><h1>Archive</h1><p>Slides, recordings, and material from contest sessions will be collected here.</p></div></section>
    <div class="wrap">
      <article class="prose">
        <p class="placeholder">Nothing here yet. Material from the IEEE VIS 2026 announcement and the IEEE VIS 2027 contest session will be added as it becomes available.</p>
      </article>
    </div>
"""

# ---------------------------------------------------------------- ACKNOWLEDGEMENTS
ACK = """
    <section class="page-title"><div class="wrap"><h1>Acknowledgements</h1><p>Organizers, collaborators, sponsor, and the people behind the dataset.</p></div></section>
    <div class="wrap page-grid">
      <aside class="toc" aria-label="On this page">
        <p>On this page</p>
        <ol>
          <li><a href="#chairs">Contest chairs</a></li>
          <li><a href="#jury">Jury</a></li>
          <li><a href="#collaboration">Collaboration</a></li>
          <li><a href="#sponsor">Sponsor</a></li>
          <li><a href="#data">Data</a></li>
          <li><a href="#references">References</a></li>
        </ol>
      </aside>
      <article class="prose">
        <h2 id="chairs">Contest chairs</h2>
        <ul class="people">
          <li><strong>Haichao Miao</strong>, Research Scientist, Lawrence Livermore National Laboratory, miao1 (at) llnl.gov</li>
          <li><strong>Shusen Liu</strong>, Research Scientist, Lawrence Livermore National Laboratory, liu42 (at) llnl.gov</li>
          <li><strong>Jenny Nicolino</strong>, Material Scientist, Lawrence Livermore National Laboratory, nicolino2 (at) llnl.gov</li>
        </ul>

        <h2 id="jury">Jury</h2>
        <p>The contest chairs will invite additional domain experts to join the jury, including:</p>
        <ul class="people">
          <li><strong>Steve Burke</strong>, Lead Engineer & SME for Metal AM, Lawrence Livermore National Laboratory</li>
          <li><strong>Massimiliano Ferrucci</strong>, NDE Engineer, Lawrence Livermore National Laboratory</li>
        </ul>

        <h2 id="sponsor">Sponsor</h2>
        <p>The $1,000 cash prize for the top entry is generously sponsored by <a href="https://www.visoar.com/">ViSOAR</a>.</p>

        <h2 id="data">Data</h2>
        <p>The Missing Struts dataset was created at Lawrence Livermore National Laboratory. Jenny Nicolino served as PI for the project. Alex Hamza originally suggested the idea, and Karl Fisher led the resonant ultrasound spectroscopy (RUS) effort, with David Stobbe performing the initial RUS work and Brian Tran later taking over analysis and paper writing. The lattice design and printing effort included work by Paul Alexander, Steve Burke, and Robert Spence, who cut the parts from the build plate.</p>
        <p>This work was performed under the auspices of the U.S. Department of Energy by Lawrence Livermore National Laboratory under contract DE-AC52-07NA27344.</p>
        <p>The contest is co-organized with <a href="https://ieeevis.org">IEEE VIS</a>. Past contests are archived at the <a href="https://sciviscontest.ieeevis.org">SciVis Contest</a> site.</p>

        <h2 id="references">References</h2>
        <ol class="references">
          <li>H. Miao, S. Narain, V. Chheang, G. Hooten, R. Seede, P. Klacansky, K. M. Bertsch, G. Guss, B. Giera, and P.-T. Bremer. <em>LatticeAnalytics: Strut-Level Visualization and Inspection of Additively Manufactured Lattice Structures.</em> IEEE Transactions on Visualization and Computer Graphics, 31(10):9266–9281, 2025. <a href="https://doi.org/10.1109/TVCG.2025.3593230">doi:10.1109/TVCG.2025.3593230</a></li>
          <li>B. Tran et al. <em>Resonant ultrasound spectroscopy measurement and modeling of additively manufactured octet truss lattice cubes.</em> NDT&amp;E International, 138:102870, 2023. <a href="https://www.osti.gov/servlets/purl/2246722">OSTI 2246722</a></li>
          <li>V. S. Deshpande, N. A. Fleck, and M. F. Ashby. <em>Effective properties of the octet-truss lattice material.</em> Journal of the Mechanics and Physics of Solids, 49(8):1747–1769, 2001.</li>
          <li>A. du Plessis, I. Yadroitsev, I. Yadroitsava, and S. G. Le Roux. <em>X-ray microcomputed tomography in additive manufacturing: A review of the current technology and applications.</em> 3D Printing and Additive Manufacturing, 5(3):227–247, 2018.</li>
          <li id="ref-ai-vis-co-scientists">H. Miao, Z. Li, K. Ai, K. Tang, C. Wang, P.-T. Bremer, and S. Liu. <em>Toward AI VIS Co-Scientists: A General and End-to-End Agent Harness for Solving Complex Data Visualization Tasks.</em> VISXGenAI Workshop (IEEE VIS), Boston, 2026.</li>
        </ol>
      </article>
    </div>
"""

# ---------------------------------------------------------------- PAST CONTESTS
PAST = [
    ("https://sciviscontest2026.github.io/", "2026: Petascale oceanic and atmospheric climate data (NASA)"),
    ("https://sciviscontest2025.github.io/", "2025: Material Science Challenge: discovery of novel materials"),
    ("https://sciviscontest2024.github.io/", "2024: Sonar Imaging for Hydrothermal Systems"),
    ("https://sciviscontest2023.github.io/", "2023: Neuronal Network Simulations of the Human Brain"),
    ("https://www.lanl.gov/projects/sciviscontest2022/index.html", "2022: Vorticity-driven Lateral Spread Ensemble Data Set"),
    ("https://scivis2021.netlify.app/", "2021: Earth's Mantle Convection"),
    ("https://kaust-vislab.github.io/SciVis2020/index.html", "2020: Transport mechanisms of eddies in the Red Sea"),
    ("https://wordpress.cels.anl.gov/2019-scivis-contest/", "2019: Cosmological simulation"),
    ("https://sciviscontest2018.org/", "2018: Deep water asteroid impacts"),
    ("https://sciviscontest.ieeevis.org/2017", "2017: Clouds and Atmospheric Processes"),
    ("https://www.uni-kl.de/sciviscontest/", "2016: Particular Ensembles"),
    ("https://darksky.slac.stanford.edu/scivis2015/", "2015: Visualize the Universe"),
    ("https://sciviscontest.ieeevis.org/2014", "2014: Volcanic eruptions and their atmospheric aftermath"),
    ("https://sciviscontest.ieeevis.org/2013", "2013: Allen Developing Mouse Brain Atlas"),
    ("https://sciviscontest.ieeevis.org/VisContest/Home.html", "2012: Computational material science"),
    ("https://sciviscontest.ieeevis.org/2011", "2011: Stability Visualization of Fluid Dynamics"),
    ("https://sciviscontest.ieeevis.org/2010", "2010: Advanced Visualization for Neurosurgical Planning"),
    (None, "2009: Deferred to 2010"),
    ("https://sciviscontest.ieeevis.org/2008", "2008: Multifield 3D Scalar Data (Astrophysics turbulence simulation data)"),
    (None, "2007: There was no contest in 2007"),
    ("https://sciviscontest.ieeevis.org/2006", "2006: See What's Shaking (Earthquake simulation data)"),
    ("https://sciviscontest.ieeevis.org/2005", "2005: Rendering Revolution (DTI and Wind data)"),
    ("https://sciviscontest.ieeevis.org/2004", "2004: Visualization Fusion (Atmospheric data)"),
]
past_items = "\n".join(
    (f'          <li><a href="{u}">{t}</a></li>' if u else f'          <li><span class="muted">{t}</span></li>')
    for u, t in PAST)
PASTCONTESTS = f"""
    <section class="page-title"><div class="wrap"><h1>Past SciVis Contests</h1><p>The contest has run as part of IEEE VIS since 2004. The full archive is maintained at <a href="https://sciviscontest.ieeevis.org">sciviscontest.ieeevis.org</a>.</p></div></section>
    <div class="wrap">
      <article class="prose">
        <ul class="past-contests">
{past_items}
        </ul>
      </article>
    </div>
"""

# ---------------------------------------------------------------- FAQS
FAQS = """
    <section class="page-title"><div class="wrap"><h1>Frequently asked questions</h1><p>Answers to the questions we expect most often. More will be added as they come in.</p></div></section>
    <div class="wrap">
      <article class="prose faq">
        <h3>Who can participate?</h3>
        <p>The contest is open worldwide to students, researchers, industry professionals, and visualization enthusiasts. Individuals and teams are both welcome; we suggest teams of about six or fewer so that authorship stays clear.</p>

        <h3>Can one team submit to both tracks?</h3>
        <p>A team may submit one entry per track, but each entry must be a distinct submission with its own report and video. The same visualization system may not be entered in both tracks.</p>

        <h3>Do I need to address every question in Tasks 1 and 2?</h3>
        <p>No. Focus on what you can do well. The jury values depth, soundness, and insight over breadth. That said, the contest is about the connection between the strut level and the part level, so entries that address only one scale will be at a disadvantage.</p>

        <h3>Do I need to work on all nine specimens?</h3>
        <p>For the Visualization Design Track, we strongly encourage it (cross-specimen comparison is part of Task 2), but you may concentrate on a subset if you explain why. For the Agentic AI Track, a CSV for every specimen is required, because the scored specimen is drawn at random after the deadline.</p>

        <h3>The STL/JSON is not aligned with the CT data. Is registration part of the challenge?</h3>
        <p>Yes, if you want it to be. One specimen is provided with a pre-aligned JSON graph so that you can develop analysis methods first. Solving registration for the remaining specimens is a legitimate contribution, as is a method that does not need the design at all.</p>

        <h3>For the Agentic AI Track, can the agent use existing visualization software?</h3>
        <p>Yes. The agent may call any tool you give it (VTK, napari, PyVista, plotting libraries, your own MCP servers). Describe in the report what the agent was given and what it created itself.</p>

        <h3>For the Agentic AI Track, may the agent write the report?</h3>
        <p>No. The report is where <em>you</em> explain the agent to us (see <a href="tasks.html#report-not-agent">the track description</a> and <a href="submissions.html#include">What to include</a>); an agent narrating its own run is not useful evidence for the jury. Agent-generated figures are welcome in the report if labeled as such.</p>

        <h3>Can I use the LatticeAnalytics paper's methods?</h3>
        <p>Absolutely. The contest is explicitly designed to build on and go beyond that work, in particular toward missing/disconnected struts and the part level.</p>
      </article>
    </div>
"""

PAGES = {
    "index.html": ("Home", HOME),
    "data.html": ("Data", DATA),
    "tasks.html": ("Tasks", TASKS),
    "submissions.html": ("Submissions", SUBMISSIONS),
    "archive.html": ("Archive", ARCHIVE),
    "acknowledgements.html": ("Acknowledgements", ACK),
    "pastcontests.html": ("Past SciVis Contests", PASTCONTESTS),
    "faqs.html": ("FAQs", FAQS),
}

os.makedirs(os.path.join(OUT, "images"), exist_ok=True)
for name in ("logo.png", "octet_truss.png", "pic_octet.jpg", "build_direction.png"):
    src = os.path.join(SRC_IMG, name)
    if os.path.exists(src):  # source images are optional once they are in website/images
        shutil.copy(src, os.path.join(OUT, "images", name))
for fn, (title, body) in PAGES.items():
    with open(os.path.join(OUT, fn), "w") as f:
        f.write(page(fn, title, body))
open(os.path.join(OUT, ".nojekyll"), "w").close()
print("wrote", len(PAGES), "pages to", OUT)
