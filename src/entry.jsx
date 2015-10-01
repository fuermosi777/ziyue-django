import React from 'react';  
import Router from 'react-router';  
import { DefaultRoute, Link, Route, RouteHandler } from 'react-router';
import AttachFastClick from 'fastclick';
//require('babel-runtime/core-js/promise')
import HomePage from './pages/HomePage.jsx';

let App = React.createClass({  
    componenetDidMount() {
        AttachFastClick(document.body);
    },

    render() {
        return ( 
            <div className="App">
                <RouteHandler/> 
            </div>
        );
    }
});

let routes = (  
    <Route name="app" path="/" handler={App}>
        <DefaultRoute handler={HomePage} />
        <Route name="category" path="/:category" handler={HomePage} />
        <Route name="post" path="/post/:pid" handler={HomePage} />
        <Route name="vendor" path="/vendor/:vid" handler={HomePage} />
    </Route>
);

Router.run(routes, Router.HistoryLocation, function (Handler) {  
    React.render(<Handler/>, document.body);
});