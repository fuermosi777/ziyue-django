import React from 'react';
import Styles from './Main.less';
import Spinner from '../Spinner/Spinner.jsx';
import Tracker from '../../utils/Tracker.js';
import $ from 'jquery';

export default React.createClass({
    propsTypes: {
        isLoading: React.PropTypes.bool,
        post: React.PropTypes.object,
        recommendPosts: React.PropTypes.array
    },

	getInitialState() {
		return {
		};
	},

    readSourceButton: null,

    componentDidMount() {
        document.body.addEventListener('click', this.handleBodyClick);
    },

    componentWillUnmount() {
        document.body.removeEventListener('click', this.handleBodyClick);
    },

    render() {
        let RecommendPosts = this.props.recommendPosts.map((item, i) => {
            return (
                <li className="recommend-post" key={i}>
                    <p className="title" onClick={this.handleRecommendPostClick.bind(this, item.id)}><i className="ion-android-arrow-dropright"></i> {item.title}</p>
                </li>
            );
        });
        return (
            <div className="Main">
                <div className="Main-wrapper">
                    {this.props.isLoading ? <Spinner/> : ''}
                    {/* post */}
                    <div className="post-wrapper">
        	            {!this.props.isLoading && this.props.post ? <div className="post-title">{this.props.post.title}</div> : ''}
                        {!this.props.isLoading && this.props.post ? <div className="post-info">
                            <img className="avatar" src={this.props.post.vendor.avatar}/>
                            <span className="vendor" onClick={this.handleVendorClick}>{this.props.post.vendor.name}</span>
                            <span className="date">{this.props.post.datetime}</span>
                        </div> : ''}
                    	{!this.props.isLoading && this.props.post ? <div className="post" dangerouslySetInnerHTML={{__html: this.props.post.body}} /> : ''}
                        {!this.props.isLoading && this.props.post ? 
                            <ul className="recommend">
                                <li className="recommend-title">相关阅读</li>
                                {RecommendPosts}
                            </ul> : ''}
                    </div>
                    {/* control */}
                    {!this.props.isLoading && this.props.post ? <div className="top-control">
                        <i className="fa fa-times-circle" onClick={this.handleCloseClick}></i>
                    </div> : ''}
                    {!this.props.isLoading && this.props.post ? <div className="bottom-control">
                        <a href={this.props.post.source} target="_blank">阅读原文 <i className="fa fa-share"></i></a>
                    </div> : ''}
                </div>
            </div> 
        );
    },

    componentDidUpdate() {
    },

    componentWillReceiveProps(props) {
    },

    shouldComponentUpdate(nextProps, nextState) {
        return true;
    },

    handleBodyClick(e) {
        if (e.target.id === 'js_view_source') {
            Tracker.trackReadSource(this.props.post.id);
        }
    },

    handleCloseClick() {
        this.props.onCloseClick();
    },

    handleVendorClick() {
        this.props.onVendorClick(this.props.post.vendorID);
    },

    handleRecommendPostClick(pid) {
        this.props.onRecommendPostSelect(pid);
    }
});