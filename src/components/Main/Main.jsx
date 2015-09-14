import React from 'react';
import Styles from './Main.less';
import Spinner from '../Spinner/Spinner.jsx';
import ScrollView from '../ScrollView/ScrollView.jsx';
import Mixpanel from '../../utils/Mixpanel.js';
import FavService from '../../services/FavService.js';
import $ from 'jquery';

export default React.createClass({
    propsTypes: {
        isLoading: React.PropTypes.bool,
        post: React.PropTypes.object,
        recommendPosts: React.PropTypes.array,
        onVendorClick: React.PropTypes.func,
        onExpandBtnClick: React.PropTypes.func,
        readingMode: React.PropTypes.bool
    },

	getInitialState() {
		return {
            favStatus: false
		};
	},

    componentDidMount() {
        // convert all links to target blank open
        let links = React.findDOMNode(this.refs.post).querySelectorAll('a');
        Array.prototype.map.call(links, (item) => {
            item.target = "_blank";
        });
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
            <div className={"Main " + (this.props.readingMode ? 'reading' : '')}>
                <div className="Main-wrapper">
                    {this.props.isLoading ? <Spinner/> : ''}
                    {/* post */}
                    <ScrollView>
        	            {!this.props.isLoading && this.props.post ? <div className="post-title">{this.props.post.title}</div> : ''}
                        {!this.props.isLoading && this.props.post ? <div className="post-info">
                            <img className="avatar" src={this.props.post.vendor.avatar}/>
                            <span className="vendor"><a href={this.props.post.vendor.url} target="_blank">{this.props.post.vendor.name}</a></span>
                            <span className="date">{this.props.post.datetime}</span>
                        </div> : ''}
                    	{!this.props.isLoading && this.props.post ? <div className="post" ref="post" dangerouslySetInnerHTML={{__html: this.props.post.body}} /> : ''}
                        {!this.props.isLoading && this.props.post ? <a href={this.props.post.source} className="read-source-button" target="_blank" onClick={this.handleReadSource}>阅读原文</a> : ''}
                        {!this.props.isLoading && this.props.post ? 
                            <ul className="recommend">
                                <li className="recommend-title">相关阅读</li>
                                {RecommendPosts}
                            </ul> : ''}
                    </ScrollView>
                    {/* control */}
                    {!this.props.isLoading && this.props.post ? <div className="top-control">
                        <i className="ion-android-close close-btn" onClick={this.handleCloseClick}></i>
                        <i className={"fav-btn " + (this.state.favStatus ? "ion-android-favorite active" : "ion-android-favorite-outline")} onClick={this.handleFavClick.bind(this, this.props.post)}></i>
                    </div> : ''}
                    {!this.props.isLoading && this.props.post ? <div className="bottom-control">
                        <i className={"expand-btn " + (this.props.readingMode ? "ion-android-contract" : "ion-android-expand")} onClick={this.handleExpandBtnClick}></i>
                        <a href={this.props.post.source} target="_blank" className="source-link" onClick={this.handleReadSource}>阅读原文 <i className="fa fa-share"></i></a>
                    </div> : ''}
                </div>
            </div> 
        );
    },

    componentDidUpdate() {
    },

    componentWillReceiveProps(props) {
        this.updateFavStatus(props.post);
    },

    shouldComponentUpdate(nextProps, nextState) {
        return true;
    },

    handleReadSource() {
        Mixpanel.trackReadSource(this.props.post.id, this.props.post.title);
    },

    handleCloseClick() {
        this.props.onCloseClick();
    },

    handleFavClick(p) {
        this.updateFavStatus(this.props.post);
        this.props.onFavClick(p);
    },

    handleVendorClick() {
        this.props.onVendorClick(this.props.post.vendorID);
    },

    handleRecommendPostClick(pid) {
        this.props.onRecommendPostSelect(pid);
    },

    handleExpandBtnClick() {
        this.props.onExpandBtnClick();
    },

    updateFavStatus(post) {
        let favStatus = !!FavService.getPost(post.id);
        this.setState({favStatus: favStatus});
    }
});