import React from 'react';
import Stylels from './VendorList.less';
import Spinner from '../Spinner/Spinner.jsx';

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
                        <div className="name">{item.name}</div>
                        <div className="bottom">{item.desc.substring(0, 60) + '...'}</div>
                    </div>
                </li>
            );
        });
        return (
            <div className="VendorList">
                <div className="VendorList-wrapper">
                    {this.props.isLoading ? <Spinner/> : ''}
                    {this.props.isLoading ? '' : <ul className="VendorList-list">
                        {VendorList}
                    </ul>}
                </div>
            </div>
        );
    },

    componentWillReceiveProps(props) {
    },

    handleVendorClick(vendor) {
        this.props.onVendorSelected(vendor.id);
    }
});