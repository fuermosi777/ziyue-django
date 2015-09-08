import React from 'react';
import InfoSidebar from '../components/InfoSidebar/InfoSidebar.jsx';
import PostList from '../components/PostList/PostList.jsx';
import Main from '../components/Main/Main.jsx';
import VendorList from '../components/VendorList/VendorList.jsx';
import NavigationBar from '../components/NavigationBar/NavigationBar.jsx';
import Constant from '../utils/Constant.js';
import {Navigation, State} from 'react-router';
import ContentService from '../services/ContentService.js';
import ReadLaterService from '../services/ReadLaterService.js';
import FavService from '../services/FavService.js';
import ThemeService from '../services/ThemeService.js';
import Processor from '../utils/Processor.js';
import Tracker from '../utils/Tracker.js';
import Styles from './HomePage.less';

export default React.createClass({
    mixins: [Navigation, State],

    getInitialState() {
        return {
            categorys: Constant.CATEGORYS,        // array
            category: null,                    // object

            readLaterNumber: ReadLaterService.getPosts().length,
            favNumber: FavService.getPosts().length,

            posts: [],                     // array
            start: 0,                       // number
            postListIsLoading: false,      // bool
            postListHasNext: false,

            post: null,                    // object
            recommendPosts: [],             // array
            mainIsLoading: false,           // bool

            vendorId: null,                // string
            vendors: [],                   // array
            vendorListIsLoading: false,

            theme: ThemeService.getCurrentTheme(),      // object
            mobileStatus: '',
            readingMode: false
        }
    },

    componentWillMount() {
        // get category from URL
        // and set to state
        if (this.isActive('category')) {
            let category = this.getParams().category || '';
            let categoryToSelect;
            if (category) {
                for (var i = 0; i < Constant.CATEGORYS.length; i++) {
                    if (Constant.CATEGORYS[i].category === category) {
                        categoryToSelect = Constant.CATEGORYS[i];
                    }
                }
            }
            this.handleCategorySelected(categoryToSelect);
        } else if (this.isActive('post')) {
            this.handleCategorySelected(Constant.CATEGORYS[0], false);
            let pid = this.getParams().pid || '';
            if (pid) {
                this.handlePostSelected(pid);
            }
        } else if (this.isActive('vendor')) {
            this.handleCategorySelected(Constant.CATEGORYS[0], false);

            let vid = this.getParams().vid || '';
            if (vid) {
                this.handleVendorSelected(vid);
            }
        } else {
            this.handleCategorySelected(Constant.CATEGORYS[0]);
        }
    },

    render() {
        return (
            <div className={`HomePage ${this.state.mobileStatus} ${this.state.theme}`}>
                <NavigationBar 
                    onMenuButtonClick={this.showInfoSidebar}/>
                {this.state.post ? 
                <Main 
                    post={this.state.post} 
                    isLoading={this.state.mainIsLoading} 
                    isActive={this.state.isMainMobileActive} 
                    onCloseClick={this.hideMain} 
                    onFavClick={this.handleFav}
                    recommendPosts={this.state.recommendPosts}
                    onVendorClick={this.handleVendorSelected}
                    onRecommendPostSelect={this.handlePostSelected}
                    onExpandBtnClick={this.handleReadingModeToggle}
                    readingMode={this.state.readingMode}/> : ''}
                {!this.state.post ? 
                <VendorList
                    vendors={this.state.vendors}
                    isLoading={this.state.vendorListIsLoading}
                    onVendorSelected={this.handleVendorSelected}/> : ''}
                <InfoSidebar 
                    categorys={this.state.categorys} 
                    selectedCategory={this.state.category} 
                    onCategorySelected={this.handleCategorySelected} 
                    onSearchVendor={this.handleSearchVendor} 
                    isMobileActive={this.state.isInfoSidebarMobileActive} 
                    onBack={this.hideInfoSidebar} 
                    onThemeSelected={this.handleThemeSelected}
                    readLaterNumber={this.state.readLaterNumber}
                    favNumber={this.state.favNumber}
                    onFavSelect={this.handleFavSelect}
                    onReadLaterSelect={this.handleReadLaterSelect}
                    readingMode={this.state.readingMode}/>
                <PostList posts={this.state.posts} 
                    isLoading={this.state.postListIsLoading} 
                    selectedPostId={this.state.postId}
                    category={this.state.category}
                    onPostSelected={this.handlePostSelected}
                    onNext={this.handleMorePosts}
                    onPrev={this.handleMorePosts}
                    start={this.state.start}
                    hasNext={this.state.postListHasNext}
                    onSearchPosts={this.handleSearchPosts}
                    onReadLaterBtnClick={this.handleReadLater}
                    readingMode={this.state.readingMode}/>
            </div>
        );
    },

    handleCategorySelected(t, shouldReplaceUrl=true) {
        this.hideInfoSidebar();
        this.setState({
            category: t,
            post: null,
            vendors: [],
            vendorId: null,
            start: 0,
            postListIsLoading: true,
            vendorListIsLoading: true
        });
        ContentService.getPosts(t.category).then((res) => {
            if (shouldReplaceUrl) {
                this.replaceWith('category', {category: t.category});
                document.title = `子阅 - ${t.name}`;
                Tracker.trackCategoryPageView(t.category);
            }
            this.setState({posts: res.data, postListHasNext: res.hasNext, postListIsLoading: false});
        });
        ContentService.getVendors(t.category).then((res) => {
            this.setState({vendors: res, vendorListIsLoading: false});
        });
    },

    handleMorePosts(more) {
        let delta = 0;
        if (more === 'next') {
            delta = 25;
        } else {
            delta = -25;
        }
        let end = this.state.start + delta;
        this.setState({postListIsLoading: true});
        let getMoreHanlder = this.state.vendorId ? ContentService.getVendorPosts(this.state.vendorId, end) : ContentService.getPosts(this.state.category.category, end);
        getMoreHanlder.then((res) => {
            if (res.hasOwnProperty('list')) res = res.list;
            this.setState({start: end, posts: res.data, postListHasNext: res.hasNext, postListIsLoading: false});
        });
    },

    handlePostSelected(pid) {
        this.showMain();
        this.setState({
            postId: pid,
            mainIsLoading: true,
            vendorListIsLoading: true
        });
        // mark as read
        let getPost = ReadLaterService.getPost(pid);
        if (getPost) {
            ReadLaterService.deletePost(pid);
        }
        this.setState({readLaterNumber: ReadLaterService.getPosts().length})
        //
        let getPostPromise = ContentService.getPost(pid);
        let getRecommendPostsPromise = ContentService.getRecommendPosts(pid);

        Promise.all([getPostPromise, getRecommendPostsPromise]).then((res) =>{
            let resPost = res[0];
            let resRecommendPosts = res[1];
            this.replaceWith('post', {pid: pid});
            document.title = `子阅 - ${resPost.vendor.name} - ${resPost.title}`;
            Tracker.trackPostPageView(pid);
            resPost.body = Processor.processPost(resPost.body);
            this.setState({
                post: resPost, 
                recommendPosts: resRecommendPosts.data,
                mainIsLoading: false,
                vendorListIsLoading: false
            });
        });
    },

    handleVendorSelected(vid) {
        this.setState({vendorId: vid, postListIsLoading: true});
        ContentService.getVendorPosts(vid).then((res) => {
            this.setState({posts: res.data});
            this.replaceWith('vendor', {vid: vid});
            document.title = `${res.name}`;
            Tracker.trackVendorPageView(vid);
            this.setState({postListIsLoading: false});
        });
    },

    handleVendorClick(vid) {
        // Main component vendor click event
        this.setState({post: null});
        this.handleVendorSelected(vid);
    },

    handleThemeSelected(t) {
        this.setState({theme: ThemeService.setTheme(t)});
    },

    handleSearchPosts(key) {
        this.setState({'postListIsLoading': true});
        ContentService.searchPosts(key).then((res) => {
            this.setState({'postListIsLoading': false, postListHasNext: res.hasNext, 'posts': res.data});
        }).catch((err) => {
            this.setState({'postListIsLoading': false, postListHasNext: false, 'posts': null});
        }); 
    },

    handleReadLater(post) {
        // from post list view
        let getPost = ReadLaterService.getPost(post.id);
        if (!getPost) {
            ReadLaterService.addPost(post);
        } else {
            ReadLaterService.deletePost(post.id);
        }
        this.setState({readLaterNumber: ReadLaterService.getPosts().length});
    },

    handleReadLaterSelect() {
        // from infosidebar view
        let postsObject = ReadLaterService.getPosts();
        document.title = `子阅 - 稍后阅读`;
        Tracker.trackReadLater();
        this.setState({posts: postsObject, postListHasNext: false, postListIsLoading: false});
    },

    handleReadingModeToggle() {
        this.setState({readingMode: !this.state.readingMode});
    },

    handleFav(post){
        // from main view
        let getPost = FavService.getPost(post.id);
        if (!getPost) {
            FavService.addPost(post);
        } else {
            FavService.deletePost(post.id);
        }
        this.setState({favNumber: FavService.getPosts().length});
    },

    handleFavSelect() {
        // from infosiderbar view
        let postsObject = FavService.getPosts();
        document.title = `子阅 - 收藏文章`;
        Tracker.trackFav();
        this.setState({posts: postsObject, postListHasNext: false, postListIsLoading: false});
    },

    showInfoSidebar() {
        this.setState({mobileStatus: 'show-info-sidebar'});
    },

    hideInfoSidebar() {
        this.setState({mobileStatus: ''});
    },

    showMain() {
        this.setState({mobileStatus: 'show-main'});
    },

    hideMain() {
        this.setState({mobileStatus: '', post: null});
    },
 });