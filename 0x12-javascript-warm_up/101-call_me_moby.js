#!/usr/bin/node

exports.callMeMoby = function (x, _Function) {
	for (let i = 0; i < x; i++) {
		_Function();
	}
};
