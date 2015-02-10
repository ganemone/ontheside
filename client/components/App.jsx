var React = require('react')
var Router = require('react-router')
var RouteHandler = Router.RouteHandler
var getNavForPath = require('../nav/index.jsx');
var MastHeadNavBar = require('./MastHeadNavBar.jsx');

var React = require('react');

var Nav = React.createClass({
  mixins: [Router.State],
  getNavItems: function() {
    return getNavForPath(this.getPathname())
  },
  render: function() {
    return (
      <MastHeadNavBar items={this.getNavItems()} brand='ontheside' />
    );
  }
});

module.exports = Nav;

var App = React.createClass({
  displayName: 'Application',
  render: function() {
    return (
      <div className="site-wrapper">
        <div className="site-wrapper-inner">
          <div className="cover-container">
            <Nav />
            <RouteHandler />
          </div>
        </div>
      </div>
    )
  }
})

module.exports = App