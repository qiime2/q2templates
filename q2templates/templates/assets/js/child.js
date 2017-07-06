// ----------------------------------------------------------------------------
// Copyright (c) 2016-2017, QIIME 2 development team.
//
// Distributed under the terms of the Modified BSD License.
//
// The full license is in the file LICENSE, distributed with this software.
// ----------------------------------------------------------------------------


document.addEventListener('DOMContentLoaded', function() {
  if (document.body.scrollHeight !== document.documentElement.scrollHeight) {
    scrollHeight = document.documentElement.scrollHeight
  } else {
    scrollHeight = document.body.scrollHeight
  }
  var height = Math.max(
    scrollHeight,
    Math.max(document.body.offsetHeight, document.documentElement.offsetHeight),
    Math.max(document.body.clientHeight, document.documentElement.clientHeight)
  );
  var height = document.documentElement.scrollHeight
  parent.postMessage(height, '*');
});
