import React from 'react';
import Styles from './Spinner.less';

export default React.createClass({
    render() {
        return(
            <div className="Spinner">
                <img src={require('./three-dots.svg')} className="Spinner-img"/>
            </div>
        );
    }
});