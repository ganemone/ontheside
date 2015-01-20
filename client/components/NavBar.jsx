/** @jsx React.DOM */
var NavBarItem = require('./NavBarItem.jsx');
var React = require('react');
var navbar = React.createClass({
  displayName: 'navbar',
  render: function() {
    return (
      <nav className="navbar navbar-default">
        <div className="container-fluid">
          <div className="navbar-header">
            <button type="button" className="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1">
              <span className="sr-only">Toggle navigation</span>
              <span className="icon-bar"></span>
              <span className="icon-bar"></span>
              <span className="icon-bar"></span>
            </button>
            <a className="navbar-brand" href="#">ontheside</a>
          </div>
          <div className="collapse navbar-collapse">
            <ul className="nav navbar-nav">
            {this.props.items.map(function(item) {
              return (<NavBarItem type={item.type} data={item.data} id={item.id} isInitiallyActive={item.isActive} />);
            })}
            </ul>
          </div>
        </div>
      </nav>
    );
  }
});
module.exports = navbar;