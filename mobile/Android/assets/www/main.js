$( function() {

  $('#show-location').bind( 'tap', function( e ) {
    alert( 'You want your location' );
    e.stopImmediatePropagation();
    return false;
  } );  

  $('body').bind( 'swipe', function( e ) {
    alert( 'You swiped!' );
    e.stopImmediatePropagation();
    return false;
  } );  

var onSuccess = function(position) {
    alert('Latitude: '          + position.coords.latitude          + '\n' +
          'Longitude: '         + position.coords.longitude         + '\n' +
          'Altitude: '          + position.coords.altitude          + '\n' +
          'Accuracy: '          + position.coords.accuracy          + '\n' +
          'Altitude Accuracy: ' + position.coords.altitudeAccuracy  + '\n' +
          'Heading: '           + position.coords.heading           + '\n' +
          'Speed: '             + position.coords.speed             + '\n' +
          'Timestamp: '         + new Date(position.timestamp)      + '\n');
};

// onError Callback receives a PositionError object
//
function onError(error) {
    alert('code: '    + error.code    + '\n' +
          'message: ' + error.message + '\n');
}

navigator.geolocation.getCurrentPosition(onSuccess, onError);

} );