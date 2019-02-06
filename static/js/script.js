
  document.getElementById('person_search').onsubmit = function() {
      window.location = 'person_search.html' + document.getElementById('person_submit').value;
      return false;
  }
