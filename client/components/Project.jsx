var React = require('react');

var Project = React.createClass({
  render: function() {
    var project = this.props.project;
    return (
      <div>
        <div className="projectName">{project.name}</div>
        <div className="projectDescription">{project.description}</div>
        <div className="projectFavoriteContainer">
          <button class="btn btn-default">Favorite</button>
          <span>{project.numFavorites}</span>
        </div>
      </div>
    );
  }
});

module.exports = Project;