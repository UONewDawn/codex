# Hues

Browse all available hues on New Dawn. Use the search box to find specific hue IDs, or adjust the number of results per page.

<link rel="stylesheet" href="https://cdn.datatables.net/1.13.7/css/jquery.dataTables.min.css">
<style>
  #hues-table {
    width: 100% !important;
  }
  #hues-table img {
    image-rendering: pixelated;
    image-rendering: -moz-crisp-edges;
    image-rendering: crisp-edges;
  }
  #hues-table .robe-img {
    width: 66px;
    height: 66px;
    cursor: pointer;
    transition: transform 0.2s;
  }
  #hues-table .robe-img:hover {
    transform: scale(1.1);
    box-shadow: 0 0 10px rgba(255,255,255,0.3);
  }
  #hues-table td {
    text-align: center;
    vertical-align: middle;
    padding: 4px !important;
  }
  #hues-table thead th {
    background-color: rgba(100, 100, 100, 0.3) !important;
    padding: 8px !important;
  }
  #hues-table tbody tr {
    background-color: rgba(50, 50, 50, 0.2);
  }
  #hues-table tbody tr:nth-child(even) {
    background-color: rgba(70, 70, 70, 0.2);
  }
  #hues-table tbody tr:hover {
    background-color: rgba(100, 100, 100, 0.3) !important;
  }
  .dataTables_wrapper {
    margin-top: 20px;
  }
  
  /* Fix dropdown background */
  .dataTables_length select,
  .dataTables_filter input {
    background-color: rgba(50, 50, 50, 0.8) !important;
    color: #fff !important;
    border: 1px solid rgba(255, 255, 255, 0.2) !important;
    padding: 4px 8px !important;
  }
  .dataTables_length select option {
    background-color: #2d2d2d !important;
    color: #fff !important;
  }
  
  /* Add spacing to top controls */
  .dataTables_length {
    padding: 10px 0 !important;
    margin-bottom: 10px !important;
  }
  .dataTables_filter {
    padding: 10px 0 !important;
    margin-bottom: 10px !important;
  }
  .dataTables_wrapper .dataTables_length,
  .dataTables_wrapper .dataTables_filter {
    display: inline-block;
  }
  
  /* Lightbox styles */
  .lightbox {
    display: none;
    position: fixed;
    z-index: 9999;
    left: 0;
    top: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.9);
    cursor: pointer;
  }
  .lightbox-content {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    max-width: 90%;
    max-height: 90%;
    image-rendering: pixelated;
    image-rendering: -moz-crisp-edges;
    image-rendering: crisp-edges;
  }
  .lightbox-close {
    position: absolute;
    top: 20px;
    right: 40px;
    color: #fff;
    font-size: 40px;
    font-weight: bold;
    cursor: pointer;
  }
  .lightbox-caption {
    position: absolute;
    bottom: 20px;
    left: 50%;
    transform: translateX(-50%);
    color: #fff;
    font-size: 18px;
    background-color: rgba(0, 0, 0, 0.7);
    padding: 10px 20px;
    border-radius: 5px;
  }
</style>

<table id="hues-table" class="display" style="width:100%">
<thead>
  <tr>
    <th>Hue ID</th>
    <th>Color Sample</th>
    <th>Robe Preview</th>
  </tr>
</thead>
<tbody>
<tr><td>1</td><td><img src="../assets/hues/1.png" loading="lazy" alt="Hue 1"></td><td><img src="../assets/hues/robe-1.png" loading="lazy" alt="Robe Hue 1" class="robe-img"></td></tr>
<tr><td>2</td><td><img src="../assets/hues/2.png" loading="lazy" alt="Hue 2"></td><td><img src="../assets/hues/robe-2.png" loading="lazy" alt="Robe Hue 2" class="robe-img"></td></tr>
<tr><td>3</td><td><img src="../assets/hues/3.png" loading="lazy" alt="Hue 3"></td><td><img src="../assets/hues/robe-3.png" loading="lazy" alt="Robe Hue 3" class="robe-img"></td></tr>
<tr><td>4</td><td><img src="../assets/hues/4.png" loading="lazy" alt="Hue 4"></td><td><img src="../assets/hues/robe-4.png" loading="lazy" alt="Robe Hue 4" class="robe-img"></td></tr>
<tr><td>5</td><td><img src="../assets/hues/5.png" loading="lazy" alt="Hue 5"></td><td><img src="../assets/hues/robe-5.png" loading="lazy" alt="Robe Hue 5" class="robe-img"></td></tr>
<tr><td>6</td><td><img src="../assets/hues/6.png" loading="lazy" alt="Hue 6"></td><td><img src="../assets/hues/robe-6.png" loading="lazy" alt="Robe Hue 6" class="robe-img"></td></tr>
<tr><td>7</td><td><img src="../assets/hues/7.png" loading="lazy" alt="Hue 7"></td><td><img src="../assets/hues/robe-7.png" loading="lazy" alt="Robe Hue 7" class="robe-img"></td></tr>
<tr><td>8</td><td><img src="../assets/hues/8.png" loading="lazy" alt="Hue 8"></td><td><img src="../assets/hues/robe-8.png" loading="lazy" alt="Robe Hue 8" class="robe-img"></td></tr>
<tr><td>9</td><td><img src="../assets/hues/9.png" loading="lazy" alt="Hue 9"></td><td><img src="../assets/hues/robe-9.png" loading="lazy" alt="Robe Hue 9" class="robe-img"></td></tr>
<tr><td>10</td><td><img src="../assets/hues/10.png" loading="lazy" alt="Hue 10"></td><td><img src="../assets/hues/robe-10.png" loading="lazy" alt="Robe Hue 10" class="robe-img"></td></tr>
<tr><td>11</td><td><img src="../assets/hues/11.png" loading="lazy" alt="Hue 11"></td><td><img src="../assets/hues/robe-11.png" loading="lazy" alt="Robe Hue 11" class="robe-img"></td></tr>
<tr><td>12</td><td><img src="../assets/hues/12.png" loading="lazy" alt="Hue 12"></td><td><img src="../assets/hues/robe-12.png" loading="lazy" alt="Robe Hue 12" class="robe-img"></td></tr>
<tr><td>13</td><td><img src="../assets/hues/13.png" loading="lazy" alt="Hue 13"></td><td><img src="../assets/hues/robe-13.png" loading="lazy" alt="Robe Hue 13" class="robe-img"></td></tr>
<tr><td>14</td><td><img src="../assets/hues/14.png" loading="lazy" alt="Hue 14"></td><td><img src="../assets/hues/robe-14.png" loading="lazy" alt="Robe Hue 14" class="robe-img"></td></tr>
<tr><td>15</td><td><img src="../assets/hues/15.png" loading="lazy" alt="Hue 15"></td><td><img src="../assets/hues/robe-15.png" loading="lazy" alt="Robe Hue 15" class="robe-img"></td></tr>
<tr><td>16</td><td><img src="../assets/hues/16.png" loading="lazy" alt="Hue 16"></td><td><img src="../assets/hues/robe-16.png" loading="lazy" alt="Robe Hue 16" class="robe-img"></td></tr>
<tr><td>17</td><td><img src="../assets/hues/17.png" loading="lazy" alt="Hue 17"></td><td><img src="../assets/hues/robe-17.png" loading="lazy" alt="Robe Hue 17" class="robe-img"></td></tr>
<tr><td>18</td><td><img src="../assets/hues/18.png" loading="lazy" alt="Hue 18"></td><td><img src="../assets/hues/robe-18.png" loading="lazy" alt="Robe Hue 18" class="robe-img"></td></tr>
<tr><td>19</td><td><img src="../assets/hues/19.png" loading="lazy" alt="Hue 19"></td><td><img src="../assets/hues/robe-19.png" loading="lazy" alt="Robe Hue 19" class="robe-img"></td></tr>
<tr><td>20</td><td><img src="../assets/hues/20.png" loading="lazy" alt="Hue 20"></td><td><img src="../assets/hues/robe-20.png" loading="lazy" alt="Robe Hue 20" class="robe-img"></td></tr>
<tr><td>21</td><td><img src="../assets/hues/21.png" loading="lazy" alt="Hue 21"></td><td><img src="../assets/hues/robe-21.png" loading="lazy" alt="Robe Hue 21" class="robe-img"></td></tr>
<tr><td>22</td><td><img src="../assets/hues/22.png" loading="lazy" alt="Hue 22"></td><td><img src="../assets/hues/robe-22.png" loading="lazy" alt="Robe Hue 22" class="robe-img"></td></tr>
<tr><td>23</td><td><img src="../assets/hues/23.png" loading="lazy" alt="Hue 23"></td><td><img src="../assets/hues/robe-23.png" loading="lazy" alt="Robe Hue 23" class="robe-img"></td></tr>
<tr><td>24</td><td><img src="../assets/hues/24.png" loading="lazy" alt="Hue 24"></td><td><img src="../assets/hues/robe-24.png" loading="lazy" alt="Robe Hue 24" class="robe-img"></td></tr>
<tr><td>25</td><td><img src="../assets/hues/25.png" loading="lazy" alt="Hue 25"></td><td><img src="../assets/hues/robe-25.png" loading="lazy" alt="Robe Hue 25" class="robe-img"></td></tr>
<tr><td>26</td><td><img src="../assets/hues/26.png" loading="lazy" alt="Hue 26"></td><td><img src="../assets/hues/robe-26.png" loading="lazy" alt="Robe Hue 26" class="robe-img"></td></tr>
<tr><td>27</td><td><img src="../assets/hues/27.png" loading="lazy" alt="Hue 27"></td><td><img src="../assets/hues/robe-27.png" loading="lazy" alt="Robe Hue 27" class="robe-img"></td></tr>
<tr><td>28</td><td><img src="../assets/hues/28.png" loading="lazy" alt="Hue 28"></td><td><img src="../assets/hues/robe-28.png" loading="lazy" alt="Robe Hue 28" class="robe-img"></td></tr>
<tr><td>29</td><td><img src="../assets/hues/29.png" loading="lazy" alt="Hue 29"></td><td><img src="../assets/hues/robe-29.png" loading="lazy" alt="Robe Hue 29" class="robe-img"></td></tr>
<tr><td>30</td><td><img src="../assets/hues/30.png" loading="lazy" alt="Hue 30"></td><td><img src="../assets/hues/robe-30.png" loading="lazy" alt="Robe Hue 30" class="robe-img"></td></tr>
<tr><td>31</td><td><img src="../assets/hues/31.png" loading="lazy" alt="Hue 31"></td><td><img src="../assets/hues/robe-31.png" loading="lazy" alt="Robe Hue 31" class="robe-img"></td></tr>
<tr><td>32</td><td><img src="../assets/hues/32.png" loading="lazy" alt="Hue 32"></td><td><img src="../assets/hues/robe-32.png" loading="lazy" alt="Robe Hue 32" class="robe-img"></td></tr>
<tr><td>33</td><td><img src="../assets/hues/33.png" loading="lazy" alt="Hue 33"></td><td><img src="../assets/hues/robe-33.png" loading="lazy" alt="Robe Hue 33" class="robe-img"></td></tr>
<tr><td>34</td><td><img src="../assets/hues/34.png" loading="lazy" alt="Hue 34"></td><td><img src="../assets/hues/robe-34.png" loading="lazy" alt="Robe Hue 34" class="robe-img"></td></tr>
<tr><td>35</td><td><img src="../assets/hues/35.png" loading="lazy" alt="Hue 35"></td><td><img src="../assets/hues/robe-35.png" loading="lazy" alt="Robe Hue 35" class="robe-img"></td></tr>
<tr><td>36</td><td><img src="../assets/hues/36.png" loading="lazy" alt="Hue 36"></td><td><img src="../assets/hues/robe-36.png" loading="lazy" alt="Robe Hue 36" class="robe-img"></td></tr>
<tr><td>37</td><td><img src="../assets/hues/37.png" loading="lazy" alt="Hue 37"></td><td><img src="../assets/hues/robe-37.png" loading="lazy" alt="Robe Hue 37" class="robe-img"></td></tr>
<tr><td>38</td><td><img src="../assets/hues/38.png" loading="lazy" alt="Hue 38"></td><td><img src="../assets/hues/robe-38.png" loading="lazy" alt="Robe Hue 38" class="robe-img"></td></tr>
<tr><td>39</td><td><img src="../assets/hues/39.png" loading="lazy" alt="Hue 39"></td><td><img src="../assets/hues/robe-39.png" loading="lazy" alt="Robe Hue 39" class="robe-img"></td></tr>
<tr><td>40</td><td><img src="../assets/hues/40.png" loading="lazy" alt="Hue 40"></td><td><img src="../assets/hues/robe-40.png" loading="lazy" alt="Robe Hue 40" class="robe-img"></td></tr>
<tr><td>41</td><td><img src="../assets/hues/41.png" loading="lazy" alt="Hue 41"></td><td><img src="../assets/hues/robe-41.png" loading="lazy" alt="Robe Hue 41" class="robe-img"></td></tr>
<tr><td>42</td><td><img src="../assets/hues/42.png" loading="lazy" alt="Hue 42"></td><td><img src="../assets/hues/robe-42.png" loading="lazy" alt="Robe Hue 42" class="robe-img"></td></tr>
<tr><td>43</td><td><img src="../assets/hues/43.png" loading="lazy" alt="Hue 43"></td><td><img src="../assets/hues/robe-43.png" loading="lazy" alt="Robe Hue 43" class="robe-img"></td></tr>
<tr><td>44</td><td><img src="../assets/hues/44.png" loading="lazy" alt="Hue 44"></td><td><img src="../assets/hues/robe-44.png" loading="lazy" alt="Robe Hue 44" class="robe-img"></td></tr>
<tr><td>45</td><td><img src="../assets/hues/45.png" loading="lazy" alt="Hue 45"></td><td><img src="../assets/hues/robe-45.png" loading="lazy" alt="Robe Hue 45" class="robe-img"></td></tr>
<tr><td>46</td><td><img src="../assets/hues/46.png" loading="lazy" alt="Hue 46"></td><td><img src="../assets/hues/robe-46.png" loading="lazy" alt="Robe Hue 46" class="robe-img"></td></tr>
<tr><td>47</td><td><img src="../assets/hues/47.png" loading="lazy" alt="Hue 47"></td><td><img src="../assets/hues/robe-47.png" loading="lazy" alt="Robe Hue 47" class="robe-img"></td></tr>
<tr><td>48</td><td><img src="../assets/hues/48.png" loading="lazy" alt="Hue 48"></td><td><img src="../assets/hues/robe-48.png" loading="lazy" alt="Robe Hue 48" class="robe-img"></td></tr>
<tr><td>49</td><td><img src="../assets/hues/49.png" loading="lazy" alt="Hue 49"></td><td><img src="../assets/hues/robe-49.png" loading="lazy" alt="Robe Hue 49" class="robe-img"></td></tr>
<tr><td>50</td><td><img src="../assets/hues/50.png" loading="lazy" alt="Hue 50"></td><td><img src="../assets/hues/robe-50.png" loading="lazy" alt="Robe Hue 50" class="robe-img"></td></tr>
</tbody>
</table>

<!-- Lightbox Modal -->
<div id="lightbox" class="lightbox">
  <span class="lightbox-close">&times;</span>
  <img class="lightbox-content" id="lightbox-img">
  <div class="lightbox-caption" id="lightbox-caption"></div>
</div>

<script src="https://code.jquery.com/jquery-3.7.1.min.js"></script>
<script src="https://cdn.datatables.net/1.13.7/js/jquery.dataTables.min.js"></script>
<script>
// Generate remaining table rows dynamically to avoid file size bloat
$(document).ready(function() {
  const tbody = $('#hues-table tbody');
  
  // Generate rows 51-3000
  for (let i = 51; i <= 3000; i++) {
    tbody.append(
      `<tr>` +
      `<td>${i}</td>` +
      `<td><img src="../assets/hues/${i}.png" loading="lazy" alt="Hue ${i}"></td>` +
      `<td><img src="../assets/hues/robe-${i}.png" loading="lazy" alt="Robe Hue ${i}" class="robe-img"></td>` +
      `</tr>`
    );
  }
  
  // Initialize DataTable
  $('#hues-table').DataTable({
    pageLength: 50,
    lengthMenu: [[25, 50, 100, 250, 500], [25, 50, 100, 250, 500]],
    order: [[0, 'asc']],
    language: {
      search: "Search Hue ID:",
      lengthMenu: "Show _MENU_ hues per page",
      info: "Showing _START_ to _END_ of _TOTAL_ hues",
      infoEmpty: "No hues found",
      infoFiltered: "(filtered from _MAX_ total hues)"
    },
    columnDefs: [
      { orderable: true, targets: 0 },
      { orderable: false, targets: [1, 2] }
    ]
  });
  
  // Lightbox functionality - only for robe images
  const lightbox = $('#lightbox');
  const lightboxImg = $('#lightbox-img');
  const lightboxCaption = $('#lightbox-caption');
  const closeBtn = $('.lightbox-close');
  
  // Click handler for robe images only (using event delegation)
  $(document).on('click', '.robe-img', function() {
    lightbox.css('display', 'block');
    lightboxImg.attr('src', $(this).attr('src'));
    lightboxCaption.text($(this).attr('alt'));
  });
  
  // Close lightbox on click
  lightbox.on('click', function() {
    lightbox.css('display', 'none');
  });
  
  // Close on escape key
  $(document).on('keydown', function(e) {
    if (e.key === 'Escape') {
      lightbox.css('display', 'none');
    }
  });
});
</script>

