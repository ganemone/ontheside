/** @jsx React.DOM */
var React = require('react');

var Cover = React.createClass({
  displayName: 'Cover',
  render: function () {
    return (
      <div className="inner cover">
        <h1 className="cover-heading">{this.props.heading}</h1>
        <p className="lead">{this.props.lead}</p>
        <p className="lead">
          <a href={this.props.action} className="btn btn-lg btn-default">Learn more</a>
        </p>
      </div>
    );
  }
});

module.exports = Cover;