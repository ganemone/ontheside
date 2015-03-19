var request = require('browser-request');

function getResponseCB(cb) {
  return function getResponseCBFunc(error, response) {
    if (error) {
      return cb(error);
    }
    return cb(null, JSON.parse(response.response));
  }
}

exports.getAll = function getAll(model, cb) {
  return request({
    uri: '/api/' + model,
    method: 'GET',
    json: true
  }, getResponseCB(cb));
};

exports.getByID = function getByID(model, id, cb) {
  return request({
    uri: '/api/' + model + '/' + id,
    method: 'GET',
    json: true
  }, getResponseCB(cb));
};

exports.insertObject = function insertObject(modelName, data, cb) {
  return request({
    uri: '/api/' + modelName,
    method: 'POST',
    json: true,
    body: data
  }, getResponseCB(cb));
};
