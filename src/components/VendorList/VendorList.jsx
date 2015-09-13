import React from 'react';
import Stylels from './VendorList.less';
import Spinner from '../Spinner/Spinner.jsx';
import ScrollView from '../ScrollView/ScrollView.jsx';
import Mixpanel from '../../utils/Mixpanel.js';

export default React.createClass({
    propsTypes: {
        isLoading: React.PropTypes.bool,
        vendors: React.PropTypes.array
    },

    getInitialState() {
        return {
        };
    },

    render() {
        let VendorList = this.props.vendors.map((item, i) => {
            return (
                <li key={i}>
                    <div className="content" onClick={this.handleVendorClick.bind(this, item)}>
                        <img src={item.avatar} className="avatar"/>
                        <div className="name">{item.name} {item.authorized ? <i className="ion-android-bookmark ribbon"/> : ''} {item.authorized ? <span className="note">授权博客</span> : ''}</div>
                        <div className="bottom">{item.desc}</div>
                    </div>
                </li>
            );
        });
        return (
            <div className="VendorList">
                <div className="wrapper">
                    <ScrollView>
                        {this.props.isLoading ? <Spinner/> : ''}
                        {this.props.isLoading ? '' : <ul className="VendorList-list">
                            {VendorList}
                        </ul>}
                    </ScrollView>
                </div>
            </div>
        );
    },

    componentWillReceiveProps(props) {
    },

    handleVendorClick(vendor) {
        this.props.onVendorSelected(vendor.id);
        Mixpanel.trackVendorClickEvent(vendor.id);
    }
});