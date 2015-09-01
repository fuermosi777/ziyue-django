import React from 'react';
import Styles from './PostList.less';
import Spinner from '../Spinner/Spinner.jsx';
import Tracker from '../../utils/Tracker.js';

const LENGTH = 25;

export default React.createClass({
    propTypes: {
        posts: React.PropTypes.array,
        selectedPostId: React.PropTypes.string,
        start: React.PropTypes.number,
        isLoading: React.PropTypes.bool,
        hasNext: React.PropTypes.bool
    },

    getInitialState() {
        return {
            shouldShowSearchInput: false,
            keyword: ''
        };
    },

    render() {
        let PostList = this.props.posts.map((item, i) => {
            return (
                <li key={i} onClick={this.handlePostClick.bind(this, item)} className={this.props.selectedPostId && this.props.selectedPostId === item.id ? 'active' : ''}>
                    <div className="top"><span className="title">{item.title}</span></div>
                    <div className="bottom"><img className="avatar" src={item.vendor.avatar}/><span className="author">{item.vendor.name}</span><span className="date">{item.datetime}</span></div>
                </li>
            );
        });

        return (            
            <div className="PostList">
                {this.props.isLoading ? <Spinner/> : ''}
                {this.props.isLoading ? '' : <ul className="PostList-list">
                    {this.props.start > 0 ? <li onClick={this.handlePrevClick}><span className="more">上一页</span></li> : ''}
                    {PostList}
                    {this.props.hasNext ? <li onClick={this.handleNextClick}><span className="more">下一页</span></li> : ''}
                </ul>}
                <div className="PostList-control">
                    {this.state.shouldShowSearchInput ? <input className="search-input" ref="searchInput" onBlur={this.handleSearchInputBlur} onChange={this.handleSearchInputChange} onKeyDown={this.handleSearchInputKeyDown}/> : ''}
                    {this.state.shouldShowSearchInput && !this.state.keyword ? <label className="search-input-label">搜索文章</label> : ''}
                    <i className="ion-search search" onClick={this.handleSearchIconClick}></i>
                </div>
            </div>
        );
    },

    handlePostClick(post) {
        this.props.onPostSelected(post.id);
        Tracker.trackPostClickEvent(post.id);
    },

    handleNextClick() {
        this.props.onNext('next');
    },

    handlePrevClick() {
        this.props.onPrev('prev');
    },

    handleSearchIconClick() {
        this.setState({shouldShowSearchInput: true}, () => {
            React.findDOMNode(this.refs.searchInput).focus();
        });
    },

    handleSearchInputBlur() {
        this.setState({shouldShowSearchInput: false});
    },

    handleSearchInputChange(e) {
        this.setState({keyword: e.target.value});
    },

    handleSearchInputKeyDown(e) {
        if (!this.state.keyword) return;
        if (e.keyCode === 13) {
            this.props.onSearchPosts(this.state.keyword);
            this.setState({keyword: '', shouldShowSearchInput: false});
        }
    },

});