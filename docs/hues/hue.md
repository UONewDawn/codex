---
title: Hue Details
---

# Hue Details

<div id="hue-content" markdown="1">
  <p style="text-align: center; color: #888;">Loading hue details...</p>
</div>

<style>
  .hue-detail-container {
    max-width: 800px;
    margin: 0 auto;
    text-align: center;
  }
  .hue-detail-container h2 {
    margin-bottom: 30px;
  }
  .hue-images {
    display: flex;
    justify-content: center;
    align-items: flex-start;
    gap: 40px;
    margin: 30px 0;
    flex-wrap: wrap;
  }
  .hue-image-section {
    flex: 1;
    min-width: 200px;
  }
  .hue-image-section h3 {
    margin-bottom: 15px;
    font-size: 1.2em;
  }
  .hue-image-section img {
    image-rendering: pixelated;
    image-rendering: -moz-crisp-edges;
    image-rendering: crisp-edges;
    max-width: 100%;
    height: auto;
    border: 1px solid rgba(255, 255, 255, 0.2);
    padding: 10px;
    background-color: rgba(50, 50, 50, 0.3);
    border-radius: 4px;
  }
  .hue-image-section.robe img {
    background-color: #000;
  }
  .back-link {
    display: inline-block;
    margin-top: 30px;
    padding: 10px 20px;
    background-color: rgba(100, 100, 100, 0.3);
    color: inherit;
    text-decoration: none;
    border-radius: 4px;
    transition: background-color 0.2s;
  }
  .back-link:hover {
    background-color: rgba(120, 120, 120, 0.4);
  }
  .error-message {
    color: #ff6b6b;
    text-align: center;
    padding: 20px;
  }
</style>

<script>
document.addEventListener('DOMContentLoaded', function() {
  const urlParams = new URLSearchParams(window.location.search);
  const hueId = urlParams.get('id');
  const contentDiv = document.getElementById('hue-content');
  
  if (!hueId) {
    contentDiv.innerHTML = `
      <div class="error-message">
        <h2>No Hue ID Specified</h2>
        <p>Please provide a hue ID in the URL. Example: <code>?id=1234</code></p>
        <a href="../" class="back-link">← Browse All Hues</a>
      </div>
    `;
    return;
  }
  
  // Validate hue ID is a number
  const hueNumber = parseInt(hueId);
  if (isNaN(hueNumber) || hueNumber < 1 || hueNumber > 3000) {
    contentDiv.innerHTML = `
      <div class="error-message">
        <h2>Invalid Hue ID</h2>
        <p>Hue ID must be a number between 1 and 3000.</p>
        <a href="../" class="back-link">← Browse All Hues</a>
      </div>
    `;
    return;
  }
  
  // Generate the hue detail page
  contentDiv.innerHTML = `
    <div class="hue-detail-container">
      <h2>Hue #${hueNumber}</h2>
      
      <div class="hue-images">
        <div class="hue-image-section">
          <h3>Color Sample</h3>
          <img src="../../assets/hues/${hueNumber}.png" alt="Hue ${hueNumber} Color Sample">
        </div>
        
        <div class="hue-image-section robe">
          <h3>Robe Preview</h3>
          <img src="../../assets/hues/robe-${hueNumber}.png" alt="Hue ${hueNumber} Robe">
        </div>
      </div>
      
      <a href="../" class="back-link">← Back to Hue List</a>
    </div>
  `;
  
  // Update page title
  document.title = `Hue #${hueNumber} - New Dawn Codex`;
});
</script>
