import React from 'react';
import Styles from './PostList.less';
import Spinner from '../Spinner/Spinner.jsx';
import ScrollView from '../ScrollView/ScrollView.jsx';
import Mixpanel from '../../utils/Mixpanel.js';
import Basic from '../../utils/Basic.js';
import ReadLaterService from '../../services/ReadLaterService.js';
import $ from 'jquery';

const LENGTH = 25;

export default React.createClass({
    propTypes: {
        posts: React.PropTypes.array,
        selectedPostId: React.PropTypes.string,
        start: React.PropTypes.number,
        isLoading: React.PropTypes.bool,
        hasNext: React.PropTypes.bool,
        readingMode: React.PropTypes.bool
    },

    getInitialState() {
        return {
            shouldShowSearchInput: false,
            keyword: '',
            readLaterStatuses: [],
            dateMarkers: []
        };
    },

    componentWillReceiveProps(props) {
        this.updateReadLaterStatuses(props.posts);
        this.updateDateMarkers(props.posts);
    },

    componentWillMount() {
        window.addEventListener('keydown', this.handleKeyDown);
    },

    componentWillUnmount() {
        window.removeEventListener('keydown', this.handleKeyDown);
    },

    componentDidMount() {
        window.addEventListener('mousewheel', () => {});
    },

    render() {
        let PostList = this.props.posts.map((item, i) => {
            let findFirst = this.state.dateMarkers.filter((it) => {
                return it.firstIndex === i;
            });
            return (
                <div key={i}>
                    {findFirst.length > 0 ? <span className="date-mark">{item.date}</span> : null}
                    <li onClick={this.handlePostClick.bind(this, item)} className={this.props.selectedPostId && this.props.selectedPostId === item.id ? 'active' : ''}>
                        <div className="top"><span className="title">{item.title}</span></div>
                        <div className="bottom"><img className="avatar" src={item.vendor.avatar}/><span className="author">{item.vendor.name}</span><i className={this.state.readLaterStatuses[i] ? "ion-ios-book active": "ion-ios-book-outline"} onClick={this.handleReadLaterBtn.bind(this, item)}></i><span className="date">{item.datetime}</span></div>
                    </li>
                </div>
            );
        });

        return (            
            <div className={"PostList " + (this.props.readingMode ? 'reading' : '')}>
                {this.props.isLoading ? <Spinner/> : ''}
                {this.props.isLoading ? '' : 
                <ScrollView>
                    {this.props.start > 0 ? <li onClick={this.handlePrevClick}><span className="more">上一页</span></li> : ''}
                    {PostList}
                    {this.props.hasNext ? <li onClick={this.handleNextClick}><span className="more">下一页</span></li> : ''}
                </ScrollView>}
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
        Mixpanel.trackPostClickEvent(post.id, post.title);
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

    handleReadLaterBtn(e, event) {
        this.props.onReadLaterBtnClick(e);
        this.updateReadLaterStatuses(this.props.posts);
        event.stopPropagation();
    },

    handleKeyDown(e) {
        if (e.keyCode === 38) {
            //up
            e.preventDefault();
            let findIndex = Basic.findPostBasedOnId(this.props.posts, this.props.selectedPostId);
            if (findIndex > 0) {
                this.handlePostClick(this.props.posts[findIndex - 1]);
            }
        } else if (e.keyCode === 40) {
            e.preventDefault();
            e.preventDefault();
            let findIndex = Basic.findPostBasedOnId(this.props.posts, this.props.selectedPostId);
            if (findIndex < this.props.posts.length - 1) {
                this.handlePostClick(this.props.posts[findIndex + 1]);
            }
        }
    },

    updateReadLaterStatuses(posts) {
        let readLaterStatuses = posts.map((item) => {
            return !!ReadLaterService.getPost(item.id);
        });
        this.setState({readLaterStatuses: readLaterStatuses});
    },

    updateDateMarkers(posts) {
        let dateMarkers = [];
        for (let i = 0; i < posts.length; i++) {
            let date = posts[i].date;
            let findDate = dateMarkers.filter((item) => {
                return item.date === date;
            });
            if (findDate.length <= 0) {
                dateMarkers.push({date: date, firstIndex: i});
            }
        }
        this.setState({dateMarkers: dateMarkers});
    }
});