var React = require('react');
var ReactAsync = require('react-async');
var Project = require('./Project.jsx');
var api = require('../models/api.js');

var ProjectList = React.createClass({
  mixins: [ReactAsync.Mixin],
  getInitialStateAsync: function(cb) {
    api.getAll('projects', cb);
  },
  render: function() {
    console.log(this.state);
    return (
      <div>
        Stuff
      </div>
    );
  }
});

// {
        //   this.state.projects.map(function(project) {
        //     return (
        //       <Project project={project} />
        //     );
        //   })
        // }

module.exports = ProjectList;