/** @jsx React.DOM */
var React = require('react');
var MastHeadNavBar = require('./MastHeadNavBar.jsx');
var Cover = require('./Cover.jsx');
var Footer = require('./Footer.jsx');
var Router = require('react-router');
var Route = Router.Route;
var RouteHandler = Router.RouteHandler;
var Link = Router.Link;

var items = [
{
  isActive: true,
  data: {
    action: '#',
    text: 'Home'
  },
  id: 0
},
{
  data: {
    action: '#',
    text: 'Login / Sign Up'
  },
  id: 1
},
{
  data: {
    action: '#',
    text: 'Browse Projects'
  },
  id: 3
}];

var lead = 'Collaborate and share your side projects with developers, designers, and other professionals from around the world.';

var app = React.createClass({

  displayName: 'app',
  render: function () {
    return (
      <div className="site-wrapper">
        <div className="site-wrapper-inner">
          <div className="cover-container">
            <MastHeadNavBar items={items} brand='ontheside' />
            <Cover heading='ontheside' lead={lead} buttonText='Learn more' action='#' />
            <Footer text='Footer text goes here :)' />
          </div>
        </div>
      </div>
    );
  }
});

module.exports = app;