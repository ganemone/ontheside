/** @jsx React.DOM */
var React = require('react')
var MastHeadNavBar = require('./MastHeadNavBar.jsx')
var Cover = require('./Cover.jsx')
var Footer = require('./Footer.jsx')

var lead = 'Collaborate and share your side projects with developers, designers, and other professionals from around the world.'

var Home = React.createClass({

  displayName: 'Home',
  render: function () {
    return (
      <div>
        <Cover heading='ontheside' lead={lead} buttonText='Learn more' action='#' />
        <Footer text='Footer text goes here :)' />
      </div>
    )
  }
})

module.exports = Home