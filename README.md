<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
  <h1>Cyclic Loading Protocol Generator for FEA Simulations</h1>

  <p>This project provides a Python-based solution for generating cyclic loading protocols for FEA simulations. The script produces a time vs. amplitude dataset based on user-defined drift percentages, cycles, and loading parameters. It outputs a CSV file compatible with various simulation software and provides a visual plot for quick validation.</p>

  <h2>Features</h2>
  <ul>
    <li><strong>User-Friendly Input:</strong> Easily define drift percentages, cycles, column height, and sampling rate through prompts.</li>
    <li><strong>Automated Data Generation:</strong> Creates a detailed time-amplitude dataset for cyclic loading.</li>
    <li><strong>CSV Export:</strong> Outputs a ready-to-use <code>.csv</code> file for simulations and further analysis.</li>
    <li><strong>Visualization:</strong> Plots the generated loading protocol for quick review and validation.</li>
  </ul>

  <h2>Usage Instructions</h2>
  <ol>
    <li>Run the script using:
      <pre><code>python cyclic_loading_generator.py</code></pre>
    </li>
    <li>Enter the required parameters when prompted (or press Enter to use default values).</li>
    <li>Review the generated file: <code>cyclic_loading_protocol.csv</code></li>
    <li>Check the plotted graph for the loading pattern and verify the data.</li>
    <li>Customize or extend the code as needed for your specific simulation software.</li>
  </ol>

  <h2>Requirements</h2>
  <p>The following Python packages are required:</p>
  <ul>
    <li>numpy</li>
    <li>pandas</li>
    <li>matplotlib</li>
  </ul>
  <p>Install dependencies using:</p>
  <pre><code>pip install numpy pandas matplotlib</code></pre>

  <h2>License</h2>
  <p>This project is licensed under the <strong>MIT License</strong>.</p>
  <p>You are free to use, modify, and distribute this software under the terms of the MIT License. If you use this software in your work, please provide appropriate credit to the developer.</p>

  <h2>Developer Information</h2>
  <ul>
    <li><strong>Developer:</strong> Engr. Tufail Mabood</li>
    <li><strong>Contact:</strong> <a href="https://wa.me/+923440907874">WhatsApp</a></li>
    <li><strong>Note:</strong> This tool is open-source. Feel free to modify it and share improvements.</li>
  </ul>
</body>
</html>
