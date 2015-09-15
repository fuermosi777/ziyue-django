import React from 'react';
import Styles from './ScrollView.less';

export default React.createClass({
    getInitialState() {
        return {
            height: 0,
            handlerScrollTop: 0,
            handlerHide: true
        };
    },

    handlerHider: null,
    scrollHandler: null,
    lastPos: 0,

    componentDidMount() {
        window.addEventListener('resize', this.handleResize);
        document.addEventListener('mousemove', this.handleHandlerMouseMove);
        document.addEventListener('mouseup', this.handleHandlerMouseUp);
        this.updateHeight();
    },

    componentWillUnmount() {
        window.removeEventListener('resize', this.removeResize);  
        document.removeEventListener('mousemove', this.handleHandlerMouseMove);
        document.removeEventListener('mouseup', this.handleHandlerMouseUp);
    },
    render() {
        return (
            <div className="ScrollView">
                <div className="scrollbar">
                    <div className={"handler " + (this.state.handlerHide ? 'hide' : '')} 
                        style={{height: '20%', top: this.state.handlerScrollTop.toString() + '%'}} 
                        onMouseDown={this.handleHandlerMouseDown}/>
                </div>
                <div className="scroller" onScroll={this.handleScroll} ref="scroller">
                    {this.props.children}
                </div>
            </div>
        );
    },

    handleScroll(e) {
        clearTimeout(this.handlerHider);
        let pos = e.target.scrollTop / (e.target.scrollHeight- this.state.height) * 0.8;
        this.setState({
            handlerScrollTop: pos * 100,
            handlerHide: false
        }, () => {
            this.handlerHider = setTimeout(() => {
                this.setState({handlerHide: true});
            }, 1500);
        });
        if (pos < 0.2 && pos < this.lastPos && this.props.onApproachingTop) {
            this.props.onApproachingTop();
        }
        if (pos > 0.6 && pos > this.lastPos && this.props.onApproachingBottom) {
            this.props.onApproachingBottom();
        }
        if (this.props.onScrolling) {
            this.props.onScrolling(pos, e.target.scrollTop);
        }
        this.lastPos = pos;
    },

    handleResize() {
        this.updateHeight();
    },

    handleHandlerMouseDown(e) {
        this.scrollHandler = e.target;
        clearTimeout(this.handlerHider);
        this.setState({handlerHide: false});
    },

    handleHandlerMouseMove(e) {
        if (this.scrollHandler) {
            let pos = (e.pageY) / this.state.height;
            pos = (pos < 0 ? 0 : (pos > 0.8 ? 0.8 : pos)) * 100;
            React.findDOMNode(this.refs.scroller).scrollTop = pos * React.findDOMNode(this.refs.scroller).scrollHeight / 100;
        }
    },

    handleHandlerMouseUp(e) {
        this.scrollHandler = null;
        clearTimeout(this.handlerHider);
        this.handlerHider = setTimeout(() => {
            this.setState({handlerHide: true});
        }, 1500);
    },

    updateHeight() {
        this.setState({height: React.findDOMNode(this).offsetHeight});  
    }

});