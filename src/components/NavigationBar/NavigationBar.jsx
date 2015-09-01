import React from 'react';
import Styles from './NavigationBar.less';

export default React.createClass({
    render() {
        return (
            <div className="NavigationBar">
                <button className="left" onClick={this.handleMenuButtonClick}>
                    <i className="fa fa-bars"></i>
                </button>
            </div>
        );
    },

    handleMenuButtonClick() {
        this.props.onMenuButtonClick();
    }
});