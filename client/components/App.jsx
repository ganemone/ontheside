var React = require('react');
var RouteHandler = require('react-router').RouteHandler;
var App = React.createClass({
  displayName: 'Application',
  render: function() {
    return (
      <div className="site-wrapper">
        <div className="site-wrapper-inner">
          <RouteHandler />
        </div>
      </div>
    );
  }
});

module.exports = App;