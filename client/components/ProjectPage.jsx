var React = require('react')
var ProjectList = require('./ProjectList.jsx')
var Footer = require('./Footer.jsx')

var ProjectPage = React.createClass({
  render: function() {
    console.log("Rendering Project page")
    return (
      <div>
        <ProjectList />
        <Footer text='Footer text goes here :)' />
      </div>
    )
  }
})

module.exports = ProjectPage