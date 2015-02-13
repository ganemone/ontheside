var React = require('react');
var ReactAsync = require('react-async');
var Project = require('./Project.jsx');
var api = require('../models/api.js');

var ProjectList = React.createClass({
  mixins: [ReactAsync.Mixin],
  getInitialState: function() {
    return {
      num_results: 0,
      page: 1,
      total_pages: 1,
      objects: []
    }
  },
  getInitialStateAsync: function(cb) {
    api.getAll('projects', cb);
  },
  render: function() {
    return (
      <div>
        {
          this.state.objects.map(function(project) {
            return (
              <Project project={project} />
            );
          })
        }
      </div>
    );
  }
});

module.exports = ProjectList;