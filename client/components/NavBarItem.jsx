/** @jsx React.DOM */
var React = require('react/addons');
var ComponentTypes = require('../constants/ComponentTypes');
var cx = React.addons.classSet;
var NavBarItem = React.createClass({
  displayName: 'NavBarItem',
  getInitialState: function() {
    return {
      isActive: false
    };
  },
  getDefaultProps: function() {
    return {
      data: {
        action: '#'
      }
    };
  },
  render: function () {
    if (this.props.type === ComponentTypes.DEFAULT) {
      return this.renderDefault();
    } else if (this.props.type === ComponentTypes.DROPDOWN) {
      return this.renderDropDown();
    } else {
      throw new Error('Invalid NavBarItem Type');
    }
  },
  renderDefault: function() {
    var classes = cx({
      'active': this.state.isActive
    });
    return (
      <li key={this.props.key} className={classes}>
        <a href={this.props.data.action}>{this.props.data.text}</a>
      </li>
    );
  },
  renderDropDown: function() {
    return (
      <li className="dropdown">
        <a href="#" className="dropdown-toggle" data-toggle="dropdown" role="button" aria-expanded="false">
          this.title
          <span className="caret"></span>
        </a>
        <ul className="dropdown-menu" role="menu">
          {this.props.data.map(function(data) {
            return (
              <li key={data.key}>
                <a href={data.action}>{data.text}</a>
              </li>
            );
          })}
        </ul>
      </li>
    );
  }
});

module.exports = NavBarItem;