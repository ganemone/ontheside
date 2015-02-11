var React = require('react')

var Project = React.createClass({
  render: function() {
    return (
      <div>
        <div className="projectName">{this.props.name}</div>
        <div className="projectDescription">{this.props.description}</div>
        <div className="projectFavoriteContainer">
          <button class="btn btn-default">Favorite</button>
          <span>{this.props.numFavorites}</span>
        </div>
      </div>
    )
  }
})

module.exports = Project