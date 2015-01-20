/** @jsx React.DOM */
var React = require('react');

var Footer = React.createClass({
  displayName: 'Footer',
  render: function () {
    return (
      <div className="mastfoot">
        <div className="inner">
          <p>{this.props.text}</p>
        </div>
      </div>
    );
  }
});

module.exports = Footer;