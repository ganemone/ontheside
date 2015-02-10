/** @jsx React.DOM */
var MastHeadNavBarItem = require('./MastHeadNavBarItem.jsx');
var React = require('react');
var navbar = React.createClass({
  displayName: 'navbar',
  render: function() {
    return (
      <div className="masthead clearfix">
        <div className="inner">
          <h3 className="masthead-brand">{this.props.brand}</h3>
          <nav>
            <ul className="nav masthead-nav">
            {this.props.items.map(function(item) {
              return (<MastHeadNavBarItem data={item.data} key={item.id} isActive={item.isActive} />);
            })}
            </ul>
          </nav>
        </div>
      </div>
    );
  }
});
module.exports = navbar;