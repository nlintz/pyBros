  


<!DOCTYPE html>
<html>
  <head prefix="og: http://ogp.me/ns# fb: http://ogp.me/ns/fb# githubog: http://ogp.me/ns/fb/githubog#">
    <meta charset='utf-8'>
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <title>pyBros/backend/pyJit.py at 49bdf9020a79799ff7667e308ae0b04cff5a7584 · nlintz/pyBros</title>
    <link rel="search" type="application/opensearchdescription+xml" href="/opensearch.xml" title="GitHub" />
    <link rel="fluid-icon" href="https://github.com/fluidicon.png" title="GitHub" />
    <link rel="shortcut icon" href="/favicon.ico" type="image/x-icon" />
    <link rel="apple-touch-icon-precomposed" sizes="57x57" href="apple-touch-icon-114.png" />
    <link rel="apple-touch-icon-precomposed" sizes="114x114" href="apple-touch-icon-114.png" />
    <link rel="apple-touch-icon-precomposed" sizes="72x72" href="apple-touch-icon-144.png" />
    <link rel="apple-touch-icon-precomposed" sizes="144x144" href="apple-touch-icon-144.png" />

    
    

    <meta content="authenticity_token" name="csrf-param" />
<meta content="KHI9Tw9lROxF8WfeNgxeEqKjCpNc9y9LckP/90ReDLE=" name="csrf-token" />

    <link href="https://a248.e.akamai.net/assets.github.com/assets/github-2ce7b3fab9fbd9a0d67ce5e4f38373b7c1abbc19.css" media="screen" rel="stylesheet" type="text/css" />
    <link href="https://a248.e.akamai.net/assets.github.com/assets/github2-f612489af1e1ee6e1cfb55a515bda8e19e3b510b.css" media="screen" rel="stylesheet" type="text/css" />
    
    


    <script src="https://a248.e.akamai.net/assets.github.com/assets/frameworks-cda884a5a58f7a231c16c075e16bc5c1509f192b.js" type="text/javascript"></script>
    
    <script defer="defer" src="https://a248.e.akamai.net/assets.github.com/assets/github-24e061385eeaff0ed974ca8bcf1dfc4fd96ab293.js" type="text/javascript"></script>
    
    

      <link rel='permalink' href='/nlintz/pyBros/blob/49bdf9020a79799ff7667e308ae0b04cff5a7584/backend/pyJit.py'>
    <meta property="og:title" content="pyBros"/>
    <meta property="og:type" content="githubog:gitrepository"/>
    <meta property="og:url" content="https://github.com/nlintz/pyBros"/>
    <meta property="og:image" content="https://a248.e.akamai.net/assets.github.com/images/gravatars/gravatar-140.png?1334862345"/>
    <meta property="og:site_name" content="GitHub"/>
    <meta property="og:description" content="Hackerz. Contribute to pyBros development by creating an account on GitHub."/>

    <meta name="description" content="Hackerz. Contribute to pyBros development by creating an account on GitHub." />

  <link href="https://github.com/nlintz/pyBros/commits/49bdf9020a79799ff7667e308ae0b04cff5a7584.atom" rel="alternate" title="Recent Commits to pyBros:49bdf9020a79799ff7667e308ae0b04cff5a7584" type="application/atom+xml" />

  </head>


  <body class="logged_in page-blob macintosh vis-public env-production ">
    <div id="wrapper">

    
    
    

      <div id="header" class="true clearfix">
        <div class="container clearfix">
          <a class="site-logo" href="https://github.com/">
            <!--[if IE]>
            <img alt="GitHub" class="github-logo" src="https://a248.e.akamai.net/assets.github.com/images/modules/header/logov7.png?1334862346" />
            <img alt="GitHub" class="github-logo-hover" src="https://a248.e.akamai.net/assets.github.com/images/modules/header/logov7-hover.png?1334862346" />
            <![endif]-->
            <img alt="GitHub" class="github-logo-4x" height="30" src="https://a248.e.akamai.net/assets.github.com/images/modules/header/logov7@4x.png?1337118066" />
            <img alt="GitHub" class="github-logo-4x-hover" height="30" src="https://a248.e.akamai.net/assets.github.com/images/modules/header/logov7@4x-hover.png?1337118066" />
          </a>



              
    <div class="topsearch  ">
        <form accept-charset="UTF-8" action="/search" id="top_search_form" method="get">
  <a href="/search" class="advanced-search tooltipped downwards" title="Advanced Search"><span class="mini-icon mini-icon-advanced-search"></span></a>
  <div class="search placeholder-field js-placeholder-field">
    <input type="text" class="search my_repos_autocompleter" id="global-search-field" name="q" results="5" spellcheck="false" autocomplete="off" data-autocomplete="my-repos-autocomplete" placeholder="Search&hellip;" data-hotkey="s" />
    <div id="my-repos-autocomplete" class="autocomplete-results">
      <ul class="js-navigation-container"></ul>
    </div>
    <input type="submit" value="Search" class="button">
    <span class="mini-icon mini-icon-search-input"></span>
  </div>
  <input type="hidden" name="type" value="Everything" />
  <input type="hidden" name="repo" value="" />
  <input type="hidden" name="langOverride" value="" />
  <input type="hidden" name="start_value" value="1" />
</form>

      <ul class="top-nav">
          <li class="explore"><a href="https://github.com/explore">Explore</a></li>
          <li><a href="https://gist.github.com">Gist</a></li>
          <li><a href="/blog">Blog</a></li>
        <li><a href="http://help.github.com">Help</a></li>
      </ul>
    </div>


            


  <div id="userbox">
    <div id="user">
      <a href="https://github.com/aletty"><img height="20" src="https://secure.gravatar.com/avatar/70ccaa5fbdf074dc3edc996ac7e0e86b?s=140&amp;d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-140.png" width="20" /></a>
      <a href="https://github.com/aletty" class="name">aletty</a>
    </div>
    <ul id="user-links">
      <li>
        <a href="/new" id="new_repo" class="tooltipped downwards" title="Create a New Repo"><span class="mini-icon mini-icon-create"></span></a>
      </li>
      <li>
        <a href="/inbox/notifications" id="notifications" class="tooltipped downwards" title="Notifications">
          <span class="mini-icon mini-icon-notifications"></span>
        </a>
      </li>
      <li>
        <a href="/settings/profile" id="account_settings"
          class="tooltipped downwards"
          title="Account Settings ">
          <span class="mini-icon mini-icon-account-settings"></span>
        </a>
      </li>
      <li>
          <a href="/logout" data-method="post" id="logout" class="tooltipped downwards" title="Sign Out">
            <span class="mini-icon mini-icon-logout"></span>
          </a>
      </li>
    </ul>
  </div>



          
        </div>
      </div>

      

            <div class="site hfeed" itemscope itemtype="http://schema.org/WebPage">
      <div class="container hentry">
        <div class="pagehead repohead instapaper_ignore readability-menu">
        <div class="title-actions-bar">
          



              <ul class="pagehead-actions">

          <li class="nspr">
            <a href="/nlintz/pyBros/pull/new/49bdf9020a79799ff7667e308ae0b04cff5a7584" class="minibutton btn-pull-request ">Pull Request</a>
          </li>


          <li class="js-toggler-container js-social-container watch-button-container on">
            <span class="watch-button"><a href="/nlintz/pyBros/toggle_watch" class="minibutton btn-watch js-toggler-target lighter" data-remote="true" data-method="post" rel="nofollow">Watch</a><a class="social-count js-social-count" href="/nlintz/pyBros/watchers">3</a></span>
            <span class="unwatch-button"><a href="/nlintz/pyBros/toggle_watch" class="minibutton btn-unwatch js-toggler-target lighter" data-remote="true" data-method="post" rel="nofollow">Unwatch</a><a class="social-count js-social-count" href="/nlintz/pyBros/watchers">3</a></span>
          </li>

              <li><a href="/nlintz/pyBros/fork" class="minibutton btn-fork js-toggler-target fork-button lighter" rel="nofollow" data-method="post">Fork</a><a href="/nlintz/pyBros/network" class="social-count">1</a>
              </li>

    </ul>

          <h1 itemscope itemtype="http://data-vocabulary.org/Breadcrumb" class="entry-title public">
            <span class="repo-label"><span>public</span></span>
            <span class="mega-icon mega-icon-public-repo"></span>
            <span class="author vcard">
<a href="/nlintz" class="url fn" itemprop="url" rel="author">              <span itemprop="title">nlintz</span>
              </a></span> /
            <strong><a href="/nlintz/pyBros" class="js-current-repository">pyBros</a></strong>
          </h1>
        </div>

          

  <ul class="tabs">
    <li><a href="/nlintz/pyBros/tree/" class="selected" highlight="repo_sourcerepo_downloadsrepo_commitsrepo_tagsrepo_branches">Code</a></li>
    <li><a href="/nlintz/pyBros/network" highlight="repo_network">Network</a>
    <li><a href="/nlintz/pyBros/pulls" highlight="repo_pulls">Pull Requests <span class='counter'>0</span></a></li>

      <li><a href="/nlintz/pyBros/issues" highlight="repo_issues">Issues <span class='counter'>0</span></a></li>

      <li><a href="/nlintz/pyBros/wiki" highlight="repo_wiki">Wiki</a></li>

    <li><a href="/nlintz/pyBros/graphs" highlight="repo_graphsrepo_contributors">Graphs</a></li>

  </ul>
  
<div class="frame frame-center tree-finder" style="display:none"
      data-tree-list-url="/nlintz/pyBros/tree-list/49bdf9020a79799ff7667e308ae0b04cff5a7584"
      data-blob-url-prefix="/nlintz/pyBros/blob/49bdf9020a79799ff7667e308ae0b04cff5a7584"
    >

  <div class="breadcrumb">
    <span class="bold"><a href="/nlintz/pyBros">pyBros</a></span> /
    <input class="tree-finder-input js-navigation-enable" type="text" name="query" autocomplete="off" spellcheck="false">
  </div>

    <div class="octotip">
      <p>
        <a href="/nlintz/pyBros/dismiss-tree-finder-help" class="dismiss js-dismiss-tree-list-help" title="Hide this notice forever" rel="nofollow">Dismiss</a>
        <span class="bold">Octotip:</span> You've activated the <em>file finder</em>
        by pressing <span class="kbd">t</span> Start typing to filter the
        file list. Use <span class="kbd badmono">↑</span> and
        <span class="kbd badmono">↓</span> to navigate,
        <span class="kbd">enter</span> to view files.
      </p>
    </div>

  <table class="tree-browser" cellpadding="0" cellspacing="0">
    <tr class="js-header"><th>&nbsp;</th><th>name</th></tr>
    <tr class="js-no-results no-results" style="display: none">
      <th colspan="2">No matching files</th>
    </tr>
    <tbody class="js-results-list js-navigation-container">
    </tbody>
  </table>
</div>

<div id="jump-to-line" style="display:none">
  <h2>Jump to Line</h2>
  <form accept-charset="UTF-8">
    <input class="textfield" type="text">
    <div class="full-button">
      <button type="submit" class="classy">
        Go
      </button>
    </div>
  </form>
</div>


<div class="subnav-bar">

  <ul class="actions subnav">
    <li><a href="/nlintz/pyBros/tags" class="blank" highlight="repo_tags">Tags <span class="counter">0</span></a></li>
    <li><a href="/nlintz/pyBros/downloads" class="blank downloads-blank" highlight="repo_downloads">Downloads <span class="counter">0</span></a></li>
    
  </ul>

  <ul class="scope">
    <li class="switcher">

      <div class="context-menu-container js-menu-container js-context-menu">
        <a href="#"
           class="minibutton bigger switcher js-menu-target js-commitish-button btn-tree repo-tree"
           data-hotkey="w"
           data-master-branch="master"
           data-ref="">
           <span><i>tree:</i> 49bdf9020a</span>
        </a>

        <div class="context-pane commitish-context js-menu-content">
          <a href="javascript:;" class="close js-menu-close"><span class="mini-icon mini-icon-remove-close"></span></a>
          <div class="context-title">Switch branches/tags</div>
          <div class="context-body pane-selector commitish-selector js-navigation-container">
            <div class="filterbar">
              <input type="text" id="context-commitish-filter-field" class="js-navigation-enable" placeholder="Filter branches/tags" data-filterable />

              <ul class="tabs">
                <li><a href="#" data-filter="branches" class="selected">Branches</a></li>
                <li><a href="#" data-filter="tags">Tags</a></li>
              </ul>
            </div>

            <div class="js-filter-tab js-filter-branches" data-filterable-for="context-commitish-filter-field" data-filterable-type=substring>
              <div class="no-results js-not-filterable">Nothing to show</div>
                <div class="commitish-item branch-commitish selector-item js-navigation-item js-navigation-target ">
                  <span class="mini-icon mini-icon-confirm"></span>
                  <h4>
                      <a href="/nlintz/pyBros/blob/master/backend/pyJit.py" class="js-navigation-open" data-name="master" rel="nofollow">master</a>
                  </h4>
                </div>
            </div>

            <div class="js-filter-tab js-filter-tags" style="display:none" data-filterable-for="context-commitish-filter-field" data-filterable-type=substring>
              <div class="no-results js-not-filterable">Nothing to show</div>
            </div>
          </div>
        </div><!-- /.commitish-context-context -->
      </div>

    </li>
  </ul>

  <ul class="subnav with-scope">

    <li><a href="/nlintz/pyBros/tree/" class="selected" highlight="repo_source">Files</a></li>
    <li><a href="/nlintz/pyBros/commits/" highlight="repo_commits">Commits</a></li>
    <li><a href="/nlintz/pyBros/branches" class="" highlight="repo_branches" rel="nofollow">Branches <span class="counter">1</span></a></li>
  </ul>

</div>

  
  
  


          

        </div><!-- /.repohead -->

        <div id="js-repo-pjax-container" data-pjax-container>
          




<!-- blob contrib key: blob_contributors:v21:80091db8d0449b579d1024ca4394ee49 -->
<!-- blob contrib frag key: views10/v8/blob_contributors:v21:80091db8d0449b579d1024ca4394ee49 -->

<!-- block_view_fragment_key: views10/v8/blob:v21:53213b6b39f934214ff7cec764dbac29 -->
  <div id="slider">

    <div class="breadcrumb" data-path="backend/pyJit.py/">
      <b itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/nlintz/pyBros/tree/49bdf9020a79799ff7667e308ae0b04cff5a7584" class="js-rewrite-sha" itemprop="url"><span itemprop="title">pyBros</span></a></b> / <span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/nlintz/pyBros/tree/49bdf9020a79799ff7667e308ae0b04cff5a7584/backend" class="js-rewrite-sha" itemscope="url"><span itemprop="title">backend</span></a></span> / <strong class="final-path">pyJit.py</strong> <span class="js-clippy mini-icon mini-icon-clippy " data-clipboard-text="backend/pyJit.py" data-copied-hint="copied!" data-copy-hint="copy to clipboard"></span>
    </div>

      
  <div class="commit file-history-tease js-blob-contributors-content" data-path="backend/pyJit.py/">
    <img class="main-avatar" height="24" src="https://secure.gravatar.com/avatar/48b9ccd96daf6feac65f1f410d7cc794?s=140&amp;d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-140.png" width="24" />
    <span class="author">Arjun</span>
    <time class="js-relative-date" datetime="2012-07-20T05:47:17-07:00" title="2012-07-20 05:47:17">July 20, 2012</time>
    <div class="commit-title">
        <a href="/nlintz/pyBros/commit/49bdf9020a79799ff7667e308ae0b04cff5a7584" class="message">improved data attr</a>
    </div>

    <div class="participation">
      <p class="quickstat"><a href="#blob_contributors_box" rel="facebox"><strong>1</strong> contributor</a></p>
      
    </div>
    <div id="blob_contributors_box" style="display:none">
      <h2>Users on GitHub who have contributed to this file</h2>
      <ul class="facebox-user-list">
        <li>
          <img height="24" src="https://secure.gravatar.com/avatar/70ccaa5fbdf074dc3edc996ac7e0e86b?s=140&amp;d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-140.png" width="24" />
          <a href="/aletty">aletty</a>
        </li>
      </ul>
    </div>
  </div>


    <div class="frames">
      <div class="frame frame-center" data-path="backend/pyJit.py/" data-permalink-url="/nlintz/pyBros/blob/49bdf9020a79799ff7667e308ae0b04cff5a7584/backend/pyJit.py" data-title="pyBros/backend/pyJit.py at 49bdf9020a79799ff7667e308ae0b04cff5a7584 · nlintz/pyBros · GitHub" data-type="blob">

        <div id="files" class="bubble">
          <div class="file">
            <div class="meta">
              <div class="info">
                <span class="icon"><b class="mini-icon mini-icon-text-file"></b></span>
                <span class="mode" title="File Mode">file</span>
                  <span>163 lines (144 sloc)</span>
                <span>3.69 kb</span>
              </div>
              <ul class="button-group actions">
                  <li>
                    <a class="grouped-button file-edit-link minibutton bigger lighter js-rewrite-sha" href="/nlintz/pyBros/edit/49bdf9020a79799ff7667e308ae0b04cff5a7584/backend/pyJit.py" data-method="post" rel="nofollow" data-hotkey="e">Edit</a>
                  </li>

                <li>
                  <a href="/nlintz/pyBros/raw/49bdf9020a79799ff7667e308ae0b04cff5a7584/backend/pyJit.py" class="minibutton btn-raw grouped-button bigger lighter" id="raw-url">Raw</a>
                </li>
                  <li>
                    <a href="/nlintz/pyBros/blame/49bdf9020a79799ff7667e308ae0b04cff5a7584/backend/pyJit.py" class="minibutton btn-blame grouped-button bigger lighter">Blame</a>
                  </li>
                <li>
                  <a href="/nlintz/pyBros/commits/49bdf9020a79799ff7667e308ae0b04cff5a7584/backend/pyJit.py" class="minibutton btn-history grouped-button bigger lighter" rel="nofollow">History</a>
                </li>
              </ul>
            </div>
              <div class="data type-python">
      <table cellpadding="0" cellspacing="0" class="lines">
        <tr>
          <td>
            <pre class="line_numbers"><span id="L1" rel="#L1">1</span>
<span id="L2" rel="#L2">2</span>
<span id="L3" rel="#L3">3</span>
<span id="L4" rel="#L4">4</span>
<span id="L5" rel="#L5">5</span>
<span id="L6" rel="#L6">6</span>
<span id="L7" rel="#L7">7</span>
<span id="L8" rel="#L8">8</span>
<span id="L9" rel="#L9">9</span>
<span id="L10" rel="#L10">10</span>
<span id="L11" rel="#L11">11</span>
<span id="L12" rel="#L12">12</span>
<span id="L13" rel="#L13">13</span>
<span id="L14" rel="#L14">14</span>
<span id="L15" rel="#L15">15</span>
<span id="L16" rel="#L16">16</span>
<span id="L17" rel="#L17">17</span>
<span id="L18" rel="#L18">18</span>
<span id="L19" rel="#L19">19</span>
<span id="L20" rel="#L20">20</span>
<span id="L21" rel="#L21">21</span>
<span id="L22" rel="#L22">22</span>
<span id="L23" rel="#L23">23</span>
<span id="L24" rel="#L24">24</span>
<span id="L25" rel="#L25">25</span>
<span id="L26" rel="#L26">26</span>
<span id="L27" rel="#L27">27</span>
<span id="L28" rel="#L28">28</span>
<span id="L29" rel="#L29">29</span>
<span id="L30" rel="#L30">30</span>
<span id="L31" rel="#L31">31</span>
<span id="L32" rel="#L32">32</span>
<span id="L33" rel="#L33">33</span>
<span id="L34" rel="#L34">34</span>
<span id="L35" rel="#L35">35</span>
<span id="L36" rel="#L36">36</span>
<span id="L37" rel="#L37">37</span>
<span id="L38" rel="#L38">38</span>
<span id="L39" rel="#L39">39</span>
<span id="L40" rel="#L40">40</span>
<span id="L41" rel="#L41">41</span>
<span id="L42" rel="#L42">42</span>
<span id="L43" rel="#L43">43</span>
<span id="L44" rel="#L44">44</span>
<span id="L45" rel="#L45">45</span>
<span id="L46" rel="#L46">46</span>
<span id="L47" rel="#L47">47</span>
<span id="L48" rel="#L48">48</span>
<span id="L49" rel="#L49">49</span>
<span id="L50" rel="#L50">50</span>
<span id="L51" rel="#L51">51</span>
<span id="L52" rel="#L52">52</span>
<span id="L53" rel="#L53">53</span>
<span id="L54" rel="#L54">54</span>
<span id="L55" rel="#L55">55</span>
<span id="L56" rel="#L56">56</span>
<span id="L57" rel="#L57">57</span>
<span id="L58" rel="#L58">58</span>
<span id="L59" rel="#L59">59</span>
<span id="L60" rel="#L60">60</span>
<span id="L61" rel="#L61">61</span>
<span id="L62" rel="#L62">62</span>
<span id="L63" rel="#L63">63</span>
<span id="L64" rel="#L64">64</span>
<span id="L65" rel="#L65">65</span>
<span id="L66" rel="#L66">66</span>
<span id="L67" rel="#L67">67</span>
<span id="L68" rel="#L68">68</span>
<span id="L69" rel="#L69">69</span>
<span id="L70" rel="#L70">70</span>
<span id="L71" rel="#L71">71</span>
<span id="L72" rel="#L72">72</span>
<span id="L73" rel="#L73">73</span>
<span id="L74" rel="#L74">74</span>
<span id="L75" rel="#L75">75</span>
<span id="L76" rel="#L76">76</span>
<span id="L77" rel="#L77">77</span>
<span id="L78" rel="#L78">78</span>
<span id="L79" rel="#L79">79</span>
<span id="L80" rel="#L80">80</span>
<span id="L81" rel="#L81">81</span>
<span id="L82" rel="#L82">82</span>
<span id="L83" rel="#L83">83</span>
<span id="L84" rel="#L84">84</span>
<span id="L85" rel="#L85">85</span>
<span id="L86" rel="#L86">86</span>
<span id="L87" rel="#L87">87</span>
<span id="L88" rel="#L88">88</span>
<span id="L89" rel="#L89">89</span>
<span id="L90" rel="#L90">90</span>
<span id="L91" rel="#L91">91</span>
<span id="L92" rel="#L92">92</span>
<span id="L93" rel="#L93">93</span>
<span id="L94" rel="#L94">94</span>
<span id="L95" rel="#L95">95</span>
<span id="L96" rel="#L96">96</span>
<span id="L97" rel="#L97">97</span>
<span id="L98" rel="#L98">98</span>
<span id="L99" rel="#L99">99</span>
<span id="L100" rel="#L100">100</span>
<span id="L101" rel="#L101">101</span>
<span id="L102" rel="#L102">102</span>
<span id="L103" rel="#L103">103</span>
<span id="L104" rel="#L104">104</span>
<span id="L105" rel="#L105">105</span>
<span id="L106" rel="#L106">106</span>
<span id="L107" rel="#L107">107</span>
<span id="L108" rel="#L108">108</span>
<span id="L109" rel="#L109">109</span>
<span id="L110" rel="#L110">110</span>
<span id="L111" rel="#L111">111</span>
<span id="L112" rel="#L112">112</span>
<span id="L113" rel="#L113">113</span>
<span id="L114" rel="#L114">114</span>
<span id="L115" rel="#L115">115</span>
<span id="L116" rel="#L116">116</span>
<span id="L117" rel="#L117">117</span>
<span id="L118" rel="#L118">118</span>
<span id="L119" rel="#L119">119</span>
<span id="L120" rel="#L120">120</span>
<span id="L121" rel="#L121">121</span>
<span id="L122" rel="#L122">122</span>
<span id="L123" rel="#L123">123</span>
<span id="L124" rel="#L124">124</span>
<span id="L125" rel="#L125">125</span>
<span id="L126" rel="#L126">126</span>
<span id="L127" rel="#L127">127</span>
<span id="L128" rel="#L128">128</span>
<span id="L129" rel="#L129">129</span>
<span id="L130" rel="#L130">130</span>
<span id="L131" rel="#L131">131</span>
<span id="L132" rel="#L132">132</span>
<span id="L133" rel="#L133">133</span>
<span id="L134" rel="#L134">134</span>
<span id="L135" rel="#L135">135</span>
<span id="L136" rel="#L136">136</span>
<span id="L137" rel="#L137">137</span>
<span id="L138" rel="#L138">138</span>
<span id="L139" rel="#L139">139</span>
<span id="L140" rel="#L140">140</span>
<span id="L141" rel="#L141">141</span>
<span id="L142" rel="#L142">142</span>
<span id="L143" rel="#L143">143</span>
<span id="L144" rel="#L144">144</span>
<span id="L145" rel="#L145">145</span>
<span id="L146" rel="#L146">146</span>
<span id="L147" rel="#L147">147</span>
<span id="L148" rel="#L148">148</span>
<span id="L149" rel="#L149">149</span>
<span id="L150" rel="#L150">150</span>
<span id="L151" rel="#L151">151</span>
<span id="L152" rel="#L152">152</span>
<span id="L153" rel="#L153">153</span>
<span id="L154" rel="#L154">154</span>
<span id="L155" rel="#L155">155</span>
<span id="L156" rel="#L156">156</span>
<span id="L157" rel="#L157">157</span>
<span id="L158" rel="#L158">158</span>
<span id="L159" rel="#L159">159</span>
<span id="L160" rel="#L160">160</span>
<span id="L161" rel="#L161">161</span>
<span id="L162" rel="#L162">162</span>
</pre>
          </td>
          <td width="100%">
                <div class="highlight"><pre><div class='line' id='LC1'><span class="kn">import</span> <span class="nn">sys</span></div><div class='line' id='LC2'><span class="kn">from</span> <span class="nn">pySQL</span> <span class="kn">import</span> <span class="o">*</span></div><div class='line' id='LC3'><span class="kn">import</span> <span class="nn">json</span></div><div class='line' id='LC4'><span class="kn">import</span> <span class="nn">os</span></div><div class='line' id='LC5'><br/></div><div class='line' id='LC6'><span class="n">color_dict</span> <span class="o">=</span> <span class="p">{</span><span class="s">&#39;Industries&#39;</span><span class="p">:</span><span class="s">&#39;D0D9C8&#39;</span><span class="p">,</span><span class="s">&#39;Financials&#39;</span><span class="p">:</span><span class="s">&#39;FDBD27&#39;</span><span class="p">,</span><span class="s">&#39;Healthcare&#39;</span><span class="p">:</span><span class="s">&#39;DA5915&#39;</span><span class="p">,</span><span class="s">&#39;ConsumerDiscretionary&#39;</span><span class="p">:</span><span class="s">&#39;4813A4&#39;</span><span class="p">,</span><span class="s">&#39;Utilities&#39;</span><span class="p">:</span><span class="s">&#39;1581F5&#39;</span><span class="p">,</span><span class="s">&#39;IT&#39;</span><span class="p">:</span><span class="s">&#39;333333&#39;</span><span class="p">,</span><span class="s">&#39;Materials&#39;</span><span class="p">:</span><span class="s">&#39;5FFF00&#39;</span><span class="p">,</span><span class="s">&#39;Energy&#39;</span><span class="p">:</span><span class="s">&#39;808099&#39;</span><span class="p">,</span><span class="s">&#39;ConsumerStaples&#39;</span><span class="p">:</span><span class="s">&#39;003399&#39;</span><span class="p">,</span><span class="s">&#39;Telecom&#39;</span><span class="p">:</span><span class="s">&#39;CCCCCC&#39;</span><span class="p">}</span></div><div class='line' id='LC7'><br/></div><div class='line' id='LC8'><span class="k">class</span> <span class="nc">node</span><span class="p">(</span><span class="nb">object</span><span class="p">):</span></div><div class='line' id='LC9'>	<span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">row</span><span class="p">,</span> <span class="n">star</span> <span class="o">=</span> <span class="bp">False</span><span class="p">):</span></div><div class='line' id='LC10'>		<span class="sd">&quot;&quot;&quot;</span></div><div class='line' id='LC11'><span class="sd">		initializes node object</span></div><div class='line' id='LC12'><span class="sd">		arg: row of SQL query data</span></div><div class='line' id='LC13'><span class="sd">		&quot;&quot;&quot;</span></div><div class='line' id='LC14'>		<span class="bp">self</span><span class="o">.</span><span class="n">id</span> <span class="o">=</span> <span class="n">row</span><span class="p">[</span><span class="s">&#39;id&#39;</span><span class="p">]</span></div><div class='line' id='LC15'>		<span class="bp">self</span><span class="o">.</span><span class="n">jitid</span> <span class="o">=</span> <span class="n">row</span><span class="p">[</span><span class="s">&#39;jitid&#39;</span><span class="p">]</span></div><div class='line' id='LC16'>		<span class="bp">self</span><span class="o">.</span><span class="n">name</span> <span class="o">=</span> <span class="n">row</span><span class="p">[</span><span class="s">&#39;name&#39;</span><span class="p">]</span></div><div class='line' id='LC17'>		<span class="bp">self</span><span class="o">.</span><span class="n">value</span> <span class="o">=</span> <span class="n">row</span><span class="p">[</span><span class="s">&#39;value&#39;</span><span class="p">]</span></div><div class='line' id='LC18'>		<span class="bp">self</span><span class="o">.</span><span class="n">adjacencies</span> <span class="o">=</span> <span class="p">[]</span></div><div class='line' id='LC19'>		<span class="bp">self</span><span class="o">.</span><span class="n">pid</span> <span class="o">=</span> <span class="bp">None</span></div><div class='line' id='LC20'>		<span class="bp">self</span><span class="o">.</span><span class="n">dct</span> <span class="o">=</span> <span class="p">{}</span></div><div class='line' id='LC21'>		<span class="bp">self</span><span class="o">.</span><span class="n">data</span></div><div class='line' id='LC22'>		<span class="bp">self</span><span class="o">.</span><span class="n">star</span> <span class="o">=</span> <span class="n">star</span></div><div class='line' id='LC23'>		<span class="bp">self</span><span class="o">.</span><span class="n">is_star</span><span class="p">()</span></div><div class='line' id='LC24'><br/></div><div class='line' id='LC25'>	<span class="k">def</span> <span class="nf">__repr__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC26'>		<span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">name</span></div><div class='line' id='LC27'>		<span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">pid</span></div><div class='line' id='LC28'><br/></div><div class='line' id='LC29'>	<span class="k">def</span> <span class="nf">is_star</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC30'>		<span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">star</span><span class="p">:</span></div><div class='line' id='LC31'>			<span class="bp">self</span><span class="o">.</span><span class="n">pid</span> <span class="o">=</span> <span class="mo">000</span></div><div class='line' id='LC32'>			<span class="bp">self</span><span class="o">.</span><span class="n">adjacencies</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">pid</span><span class="p">)</span></div><div class='line' id='LC33'><br/></div><div class='line' id='LC34'>	<span class="k">def</span> <span class="nf">star_data</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="n">color_dict</span><span class="p">):</span></div><div class='line' id='LC35'>		<span class="bp">self</span><span class="o">.</span><span class="n">data</span><span class="p">[</span><span class="s">&#39;ticker&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">jitid</span></div><div class='line' id='LC36'>		<span class="k">for</span> <span class="n">n</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">adjacencies</span><span class="p">:</span></div><div class='line' id='LC37'>			<span class="k">if</span> <span class="n">n</span><span class="o">.</span><span class="n">name</span> <span class="o">==</span> <span class="s">&#39;fin info&#39;</span><span class="p">:</span></div><div class='line' id='LC38'>				<span class="bp">self</span><span class="o">.</span><span class="n">data</span><span class="p">[</span><span class="s">&#39;price&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">n</span><span class="o">.</span><span class="n">data</span><span class="p">[</span><span class="s">&#39;price&#39;</span><span class="p">]</span></div><div class='line' id='LC39'>				<span class="bp">self</span><span class="o">.</span><span class="n">data</span><span class="p">[</span><span class="s">&#39;sector&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">n</span><span class="o">.</span><span class="n">data</span><span class="p">[</span><span class="s">&#39;sector&#39;</span><span class="p">]</span></div><div class='line' id='LC40'>				<span class="k">break</span></div><div class='line' id='LC41'>		<span class="bp">self</span><span class="o">.</span><span class="n">prep_data</span><span class="p">(</span><span class="n">color_dict</span><span class="p">)</span></div><div class='line' id='LC42'><br/></div><div class='line' id='LC43'>	<span class="k">def</span> <span class="nf">planet_data</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="n">color_dict</span><span class="p">):</span></div><div class='line' id='LC44'>		<span class="k">for</span> <span class="n">n</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">adjacencies</span><span class="p">:</span></div><div class='line' id='LC45'>			<span class="bp">self</span><span class="o">.</span><span class="n">data</span><span class="p">[</span><span class="n">n</span><span class="o">.</span><span class="n">name</span><span class="p">]</span> <span class="o">=</span> <span class="n">n</span><span class="o">.</span><span class="n">value</span></div><div class='line' id='LC46'>		<span class="bp">self</span><span class="o">.</span><span class="n">prep_data</span><span class="p">(</span><span class="n">color_dict</span><span class="p">)</span></div><div class='line' id='LC47'>		<span class="bp">self</span><span class="o">.</span><span class="n">adjacencies</span> <span class="o">=</span> <span class="p">[]</span></div><div class='line' id='LC48'><br/></div><div class='line' id='LC49'>	<span class="k">def</span> <span class="nf">add_child</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="n">n</span><span class="p">):</span></div><div class='line' id='LC50'>		<span class="sd">&quot;&quot;&quot;</span></div><div class='line' id='LC51'><span class="sd">		adds child to adjacencies list</span></div><div class='line' id='LC52'><span class="sd">		&quot;&quot;&quot;</span></div><div class='line' id='LC53'>		<span class="bp">self</span><span class="o">.</span><span class="n">adjacencies</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">n</span><span class="p">)</span></div><div class='line' id='LC54'>		<span class="n">n</span><span class="o">.</span><span class="n">pid</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">id</span>		</div><div class='line' id='LC55'>	<span class="k">def</span> <span class="nf">is_parent</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC56'>		<span class="sd">&quot;&quot;&quot;</span></div><div class='line' id='LC57'><span class="sd">		checks if node has children</span></div><div class='line' id='LC58'><span class="sd">		returns boolean</span></div><div class='line' id='LC59'><span class="sd">		&quot;&quot;&quot;</span></div><div class='line' id='LC60'>		<span class="k">if</span> <span class="n">get_childs_by_pid</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">id</span><span class="p">):</span></div><div class='line' id='LC61'>			<span class="k">return</span> <span class="bp">True</span></div><div class='line' id='LC62'>		<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC63'>			<span class="k">return</span> <span class="bp">False</span></div><div class='line' id='LC64'>	<span class="k">def</span> <span class="nf">generate_adjacency_id</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC65'>		<span class="n">adj_id</span><span class="o">=</span> <span class="p">[]</span></div><div class='line' id='LC66'>		<span class="k">for</span> <span class="n">childs</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">adjacencies</span><span class="p">:</span></div><div class='line' id='LC67'>			<span class="n">adj_id</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">childs</span><span class="o">.</span><span class="n">jitid</span><span class="p">)</span></div><div class='line' id='LC68'>		<span class="k">return</span> <span class="n">adj_id</span></div><div class='line' id='LC69'><br/></div><div class='line' id='LC70'>	<span class="k">def</span> <span class="nf">prep_data</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="n">color_dict</span><span class="p">):</span></div><div class='line' id='LC71'>		<span class="bp">self</span><span class="o">.</span><span class="n">data</span><span class="p">[</span><span class="s">&#39;dim&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="mf">0.7</span><span class="o">*</span><span class="p">(</span><span class="nb">float</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">data</span><span class="p">[</span><span class="s">&#39;price&#39;</span><span class="p">]))</span></div><div class='line' id='LC72'>		<span class="bp">self</span><span class="o">.</span><span class="n">data</span><span class="p">[</span><span class="s">&#39;$color&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">color_dict</span><span class="p">[</span><span class="bp">self</span><span class="o">.</span><span class="n">data</span><span class="p">[</span><span class="s">&#39;sector&#39;</span><span class="p">]]</span></div><div class='line' id='LC73'>		<span class="bp">self</span><span class="o">.</span><span class="n">data</span><span class="p">[</span><span class="s">&#39;star&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">star</span></div><div class='line' id='LC74'><br/></div><div class='line' id='LC75'>	<span class="k">def</span> <span class="nf">prep_JSON</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC76'>		<span class="bp">self</span><span class="o">.</span><span class="n">dct</span> <span class="o">=</span> <span class="p">{</span></div><div class='line' id='LC77'>		<span class="s">&#39;jitid&#39;</span><span class="p">:</span><span class="bp">self</span><span class="o">.</span><span class="n">jitid</span><span class="p">,</span></div><div class='line' id='LC78'>		<span class="s">&#39;name&#39;</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">name</span><span class="p">,</span></div><div class='line' id='LC79'>		<span class="s">&#39;data&#39;</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">data</span><span class="p">,</span></div><div class='line' id='LC80'>		<span class="s">&#39;adjacencies&#39;</span><span class="p">:</span><span class="bp">self</span><span class="o">.</span><span class="n">generate_adjacency_id</span><span class="p">()</span></div><div class='line' id='LC81'>		<span class="p">}</span></div><div class='line' id='LC82'><br/></div><div class='line' id='LC83'><span class="k">def</span> <span class="nf">create_star</span><span class="p">(</span><span class="n">jitid</span><span class="p">):</span></div><div class='line' id='LC84'>	<span class="sd">&quot;&quot;&quot;</span></div><div class='line' id='LC85'><span class="sd">	creates star/company</span></div><div class='line' id='LC86'><span class="sd">	args: requires companies jitID</span></div><div class='line' id='LC87'><span class="sd">	return: list of all nodes in system</span></div><div class='line' id='LC88'><span class="sd">	&quot;&quot;&quot;</span></div><div class='line' id='LC89'>	<span class="n">row</span> <span class="o">=</span> <span class="n">get_node_by_jitid</span><span class="p">(</span><span class="n">jitid</span><span class="p">)</span></div><div class='line' id='LC90'>	<span class="n">n</span> <span class="o">=</span> <span class="n">node</span><span class="p">(</span><span class="n">row</span><span class="p">,</span> <span class="n">star</span> <span class="o">=</span> <span class="bp">True</span><span class="p">)</span></div><div class='line' id='LC91'>	<span class="n">system</span> <span class="o">=</span> <span class="p">[</span><span class="n">n</span><span class="p">]</span></div><div class='line' id='LC92'>	<span class="k">if</span> <span class="n">n</span><span class="o">.</span><span class="n">is_parent</span><span class="p">():</span></div><div class='line' id='LC93'>		<span class="n">system</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span><span class="n">create_system</span><span class="p">(</span><span class="n">n</span><span class="p">))</span></div><div class='line' id='LC94'>	<span class="k">return</span> <span class="n">system</span></div><div class='line' id='LC95'><br/></div><div class='line' id='LC96'><span class="k">def</span> <span class="nf">create_system</span><span class="p">(</span><span class="n">parent</span><span class="p">):</span></div><div class='line' id='LC97'>	<span class="sd">&quot;&quot;&quot;</span></div><div class='line' id='LC98'><span class="sd">	creates childs of parent node recursively</span></div><div class='line' id='LC99'><span class="sd">	args: node object</span></div><div class='line' id='LC100'><span class="sd">	returns list of all children node for given parent node</span></div><div class='line' id='LC101'><span class="sd">	&quot;&quot;&quot;</span></div><div class='line' id='LC102'>	<span class="n">system</span> <span class="o">=</span> <span class="p">[]</span></div><div class='line' id='LC103'>	<span class="n">child_list</span> <span class="o">=</span> <span class="n">get_childs_by_pid</span><span class="p">(</span><span class="n">parent</span><span class="o">.</span><span class="n">id</span><span class="p">)</span></div><div class='line' id='LC104'>	<span class="k">for</span> <span class="n">childs</span> <span class="ow">in</span> <span class="n">child_list</span><span class="p">:</span></div><div class='line' id='LC105'>		<span class="n">row</span> <span class="o">=</span> <span class="n">get_node_by_id</span><span class="p">(</span><span class="n">childs</span><span class="p">[</span><span class="s">&#39;chid&#39;</span><span class="p">])</span></div><div class='line' id='LC106'>		<span class="n">p</span> <span class="o">=</span> <span class="n">node</span><span class="p">(</span><span class="n">row</span><span class="p">)</span></div><div class='line' id='LC107'>		<span class="n">parent</span><span class="o">.</span><span class="n">add_child</span><span class="p">(</span><span class="n">p</span><span class="p">)</span></div><div class='line' id='LC108'>		<span class="n">system</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">p</span><span class="p">)</span></div><div class='line' id='LC109'>		<span class="k">if</span> <span class="n">p</span><span class="o">.</span><span class="n">is_parent</span><span class="p">():</span></div><div class='line' id='LC110'>			<span class="n">system</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span><span class="n">create_system</span><span class="p">(</span><span class="n">p</span><span class="p">))</span></div><div class='line' id='LC111'>		<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC112'>			<span class="k">continue</span></div><div class='line' id='LC113'>	<span class="k">return</span> <span class="n">system</span></div><div class='line' id='LC114'><br/></div><div class='line' id='LC115'><span class="k">def</span> <span class="nf">create_universe</span><span class="p">(</span><span class="n">companies</span><span class="p">):</span></div><div class='line' id='LC116'>	<span class="n">universe</span> <span class="o">=</span><span class="p">[]</span></div><div class='line' id='LC117'>	<span class="k">for</span> <span class="n">jitid</span> <span class="ow">in</span> <span class="n">companies</span><span class="p">:</span></div><div class='line' id='LC118'>		<span class="n">system</span> <span class="o">=</span> <span class="n">create_star</span><span class="p">(</span><span class="n">jitid</span><span class="p">)</span></div><div class='line' id='LC119'>		<span class="n">universe</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">system</span><span class="p">)</span></div><div class='line' id='LC120'>	<span class="k">return</span> <span class="n">universe</span></div><div class='line' id='LC121'><br/></div><div class='line' id='LC122'><span class="k">def</span> <span class="nf">create_data</span><span class="p">(</span><span class="n">systems</span><span class="p">,</span> <span class="n">color_dict</span><span class="p">):</span></div><div class='line' id='LC123'>	<span class="k">for</span> <span class="n">nodes</span> <span class="ow">in</span> <span class="n">systems</span><span class="p">:</span></div><div class='line' id='LC124'>		<span class="k">if</span> <span class="n">nodes</span><span class="o">.</span><span class="n">star</span><span class="p">:</span></div><div class='line' id='LC125'>			<span class="n">ind</span> <span class="o">=</span> <span class="n">systems</span><span class="o">.</span><span class="n">index</span><span class="p">(</span><span class="n">nodes</span><span class="p">)</span></div><div class='line' id='LC126'>		<span class="k">else</span> <span class="n">nodes</span><span class="o">.</span><span class="n">star</span><span class="p">:</span></div><div class='line' id='LC127'>			<span class="n">nodes</span><span class="o">.</span><span class="n">planet_data</span><span class="p">(</span><span class="n">color_dict</span><span class="p">)</span></div><div class='line' id='LC128'>	<span class="n">systems</span><span class="p">[</span><span class="n">i</span><span class="p">]</span><span class="o">.</span><span class="n">star_data</span><span class="p">(</span><span class="n">color_dict</span><span class="p">)</span></div><div class='line' id='LC129'>	<span class="k">return</span> <span class="n">systems</span></div><div class='line' id='LC130'><br/></div><div class='line' id='LC131'><span class="k">def</span> <span class="nf">create_JSON</span><span class="p">(</span><span class="n">systems</span><span class="p">):</span></div><div class='line' id='LC132'>	<span class="k">for</span> <span class="n">nodes</span> <span class="ow">in</span> <span class="n">systems</span><span class="p">:</span></div><div class='line' id='LC133'>		<span class="k">if</span> <span class="n">nodes</span><span class="o">.</span><span class="n">pid</span> <span class="o">==</span> <span class="mo">000</span><span class="p">:</span></div><div class='line' id='LC134'>			<span class="n">ind</span> <span class="o">=</span> <span class="n">systems</span><span class="o">.</span><span class="n">index</span><span class="p">(</span><span class="n">nodes</span><span class="p">)</span></div><div class='line' id='LC135'>			<span class="n">fName</span> <span class="o">=</span> <span class="n">systems</span><span class="p">[</span><span class="n">ind</span><span class="p">]</span><span class="o">.</span><span class="n">name</span> <span class="o">+</span> <span class="s">&quot;.json&quot;</span></div><div class='line' id='LC136'>			<span class="k">break</span></div><div class='line' id='LC137'>	<span class="n">fp</span> <span class="o">=</span> <span class="nb">open</span><span class="p">(</span><span class="n">fName</span><span class="p">,</span> <span class="s">&#39;w&#39;</span><span class="p">)</span></div><div class='line' id='LC138'>	<span class="k">for</span> <span class="n">nodes</span> <span class="ow">in</span> <span class="n">systems</span><span class="p">:</span></div><div class='line' id='LC139'>		<span class="n">nodes</span><span class="o">.</span><span class="n">generate_JSON</span><span class="p">()</span></div><div class='line' id='LC140'>		<span class="n">json</span><span class="o">.</span><span class="n">dump</span><span class="p">(</span><span class="n">nodes</span><span class="o">.</span><span class="n">dct</span><span class="p">,</span><span class="n">fp</span><span class="p">)</span></div><div class='line' id='LC141'>		<span class="n">fp</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="s">&#39;</span><span class="se">\n</span><span class="s">&#39;</span><span class="p">)</span></div><div class='line' id='LC142'>	<span class="n">fp</span><span class="o">.</span><span class="n">close</span><span class="p">()</span></div><div class='line' id='LC143'><br/></div><div class='line' id='LC144'><span class="k">def</span> <span class="nf">write_json</span><span class="p">(</span><span class="n">universe</span><span class="p">,</span> <span class="n">color_dict</span><span class="p">):</span></div><div class='line' id='LC145'>	<span class="k">for</span> <span class="n">systems</span> <span class="ow">in</span> <span class="n">universe</span><span class="p">:</span></div><div class='line' id='LC146'>		<span class="n">systems</span> <span class="o">=</span> <span class="n">create_data</span><span class="p">(</span><span class="n">systems</span><span class="p">,</span> <span class="n">color_dict</span><span class="p">)</span></div><div class='line' id='LC147'>		<span class="n">create_JSON</span><span class="p">(</span><span class="n">systems</span><span class="p">)</span></div><div class='line' id='LC148'><br/></div><div class='line' id='LC149'><span class="k">def</span> <span class="nf">main</span><span class="p">(</span><span class="n">companies</span><span class="p">):</span></div><div class='line' id='LC150'>	<span class="sd">&quot;&quot;&quot;</span></div><div class='line' id='LC151'><span class="sd">	runs all functions</span></div><div class='line' id='LC152'><span class="sd">	args: list of jitids where jitid is ticker symbol of company</span></div><div class='line' id='LC153'><span class="sd">	prints json structure of node</span></div><div class='line' id='LC154'><span class="sd">	&quot;&quot;&quot;</span></div><div class='line' id='LC155'><br/></div><div class='line' id='LC156'>	<span class="k">if</span> <span class="nb">type</span><span class="p">(</span><span class="n">companies</span><span class="p">)</span> <span class="o">!=</span> <span class="nb">list</span><span class="p">:</span></div><div class='line' id='LC157'>		<span class="n">companies</span> <span class="o">=</span> <span class="p">[</span><span class="n">companies</span><span class="p">]</span></div><div class='line' id='LC158'>	<span class="n">universe</span> <span class="o">=</span> <span class="n">create_universe</span><span class="p">(</span><span class="n">companies</span><span class="p">)</span>	</div><div class='line' id='LC159'>	<span class="n">write_json</span><span class="p">(</span><span class="n">universe</span><span class="p">)</span></div><div class='line' id='LC160'><br/></div><div class='line' id='LC161'><span class="k">if</span> <span class="n">__name__</span> <span class="o">==</span> <span class="s">&quot;__main__&quot;</span><span class="p">:</span></div><div class='line' id='LC162'>	<span class="n">main</span><span class="p">(</span><span class="n">sys</span><span class="o">.</span><span class="n">argv</span><span class="p">[</span><span class="mi">1</span><span class="p">])</span></div></pre></div>
          </td>
        </tr>
      </table>
  </div>

          </div>
        </div>
      </div>
    </div>

  </div>

<div class="frame frame-loading large-loading-area" style="display:none;" data-tree-list-url="/nlintz/pyBros/tree-list/49bdf9020a79799ff7667e308ae0b04cff5a7584" data-blob-url-prefix="/nlintz/pyBros/blob/49bdf9020a79799ff7667e308ae0b04cff5a7584">
  <img src="https://a248.e.akamai.net/assets.github.com/images/spinners/octocat-spinner-64.gif?1334862346" height="64" width="64">
</div>

        </div>
      </div>
      <div class="context-overlay"></div>
    </div>

      <div id="footer-push"></div><!-- hack for sticky footer -->
    </div><!-- end of wrapper - hack for sticky footer -->

      <!-- footer -->
      <div id="footer" >
        
  <div class="upper_footer">
     <div class="container clearfix">

       <!--[if IE]><h4 id="blacktocat_ie">GitHub Links</h4><![endif]-->
       <![if !IE]><h4 id="blacktocat">GitHub Links</h4><![endif]>

       <ul class="footer_nav">
         <h4>GitHub</h4>
         <li><a href="https://github.com/about">About</a></li>
         <li><a href="https://github.com/blog">Blog</a></li>
         <li><a href="https://github.com/features">Features</a></li>
         <li><a href="https://github.com/contact">Contact &amp; Support</a></li>
         <li><a href="https://github.com/training">Training</a></li>
         <li><a href="http://enterprise.github.com/">GitHub Enterprise</a></li>
         <li><a href="http://status.github.com/">Site Status</a></li>
       </ul>

       <ul class="footer_nav">
         <h4>Clients</h4>
         <li><a href="http://mac.github.com/">GitHub for Mac</a></li>
         <li><a href="http://windows.github.com/">GitHub for Windows</a></li>
         <li><a href="http://eclipse.github.com/">GitHub for Eclipse</a></li>
         <li><a href="http://mobile.github.com/">GitHub Mobile Apps</a></li>
       </ul>

       <ul class="footer_nav">
         <h4>Tools</h4>
         <li><a href="http://get.gaug.es/">Gauges: Web analytics</a></li>
         <li><a href="http://speakerdeck.com">Speaker Deck: Presentations</a></li>
         <li><a href="https://gist.github.com">Gist: Code snippets</a></li>

         <h4 class="second">Extras</h4>
         <li><a href="http://jobs.github.com/">Job Board</a></li>
         <li><a href="http://shop.github.com/">GitHub Shop</a></li>
         <li><a href="http://octodex.github.com/">The Octodex</a></li>
       </ul>

       <ul class="footer_nav">
         <h4>Documentation</h4>
         <li><a href="http://help.github.com/">GitHub Help</a></li>
         <li><a href="http://developer.github.com/">Developer API</a></li>
         <li><a href="http://github.github.com/github-flavored-markdown/">GitHub Flavored Markdown</a></li>
         <li><a href="http://pages.github.com/">GitHub Pages</a></li>
       </ul>

     </div><!-- /.site -->
  </div><!-- /.upper_footer -->

<div class="lower_footer">
  <div class="container clearfix">
    <!--[if IE]><div id="legal_ie"><![endif]-->
    <![if !IE]><div id="legal"><![endif]>
      <ul>
          <li><a href="https://github.com/site/terms">Terms of Service</a></li>
          <li><a href="https://github.com/site/privacy">Privacy</a></li>
          <li><a href="https://github.com/security">Security</a></li>
      </ul>

      <p>&copy; 2012 <span title="0.06965s from fe13.rs.github.com">GitHub</span> Inc. All rights reserved.</p>
    </div><!-- /#legal or /#legal_ie-->

      <div class="sponsor">
        <a href="http://www.rackspace.com" class="logo">
          <img alt="Dedicated Server" height="36" src="https://a248.e.akamai.net/assets.github.com/images/modules/footer/rackspaces_logo.png?1334862346" width="38" />
        </a>
        Powered by the <a href="http://www.rackspace.com ">Dedicated
        Servers</a> and<br/> <a href="http://www.rackspacecloud.com">Cloud
        Computing</a> of Rackspace Hosting<span>&reg;</span>
      </div>
  </div><!-- /.site -->
</div><!-- /.lower_footer -->

      </div><!-- /#footer -->

    

<div id="keyboard_shortcuts_pane" class="instapaper_ignore readability-extra" style="display:none">
  <h2>Keyboard Shortcuts <small><a href="#" class="js-see-all-keyboard-shortcuts">(see all)</a></small></h2>

  <div class="columns threecols">
    <div class="column first">
      <h3>Site wide shortcuts</h3>
      <dl class="keyboard-mappings">
        <dt>s</dt>
        <dd>Focus site search</dd>
      </dl>
      <dl class="keyboard-mappings">
        <dt>?</dt>
        <dd>Bring up this help dialog</dd>
      </dl>
    </div><!-- /.column.first -->

    <div class="column middle" style='display:none'>
      <h3>Commit list</h3>
      <dl class="keyboard-mappings">
        <dt>j</dt>
        <dd>Move selection down</dd>
      </dl>
      <dl class="keyboard-mappings">
        <dt>k</dt>
        <dd>Move selection up</dd>
      </dl>
      <dl class="keyboard-mappings">
        <dt>c <em>or</em> o <em>or</em> enter</dt>
        <dd>Open commit</dd>
      </dl>
      <dl class="keyboard-mappings">
        <dt>y</dt>
        <dd>Expand URL to its canonical form</dd>
      </dl>
    </div><!-- /.column.first -->

    <div class="column last js-hidden-pane" style='display:none'>
      <h3>Pull request list</h3>
      <dl class="keyboard-mappings">
        <dt>j</dt>
        <dd>Move selection down</dd>
      </dl>
      <dl class="keyboard-mappings">
        <dt>k</dt>
        <dd>Move selection up</dd>
      </dl>
      <dl class="keyboard-mappings">
        <dt>o <em>or</em> enter</dt>
        <dd>Open issue</dd>
      </dl>
      <dl class="keyboard-mappings">
        <dt><span class="platform-mac">⌘</span><span class="platform-other">ctrl</span> <em>+</em> enter</dt>
        <dd>Submit comment</dd>
      </dl>
    </div><!-- /.columns.last -->

  </div><!-- /.columns.equacols -->

  <div class="js-hidden-pane" style='display:none'>
    <div class="rule"></div>

    <h3>Issues</h3>

    <div class="columns threecols">
      <div class="column first">
        <dl class="keyboard-mappings">
          <dt>j</dt>
          <dd>Move selection down</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>k</dt>
          <dd>Move selection up</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>x</dt>
          <dd>Toggle selection</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>o <em>or</em> enter</dt>
          <dd>Open issue</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt><span class="platform-mac">⌘</span><span class="platform-other">ctrl</span> <em>+</em> enter</dt>
          <dd>Submit comment</dd>
        </dl>
      </div><!-- /.column.first -->
      <div class="column last">
        <dl class="keyboard-mappings">
          <dt>c</dt>
          <dd>Create issue</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>l</dt>
          <dd>Create label</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>i</dt>
          <dd>Back to inbox</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>u</dt>
          <dd>Back to issues</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>/</dt>
          <dd>Focus issues search</dd>
        </dl>
      </div>
    </div>
  </div>

  <div class="js-hidden-pane" style='display:none'>
    <div class="rule"></div>

    <h3>Issues Dashboard</h3>

    <div class="columns threecols">
      <div class="column first">
        <dl class="keyboard-mappings">
          <dt>j</dt>
          <dd>Move selection down</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>k</dt>
          <dd>Move selection up</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>o <em>or</em> enter</dt>
          <dd>Open issue</dd>
        </dl>
      </div><!-- /.column.first -->
    </div>
  </div>

  <div class="js-hidden-pane" style='display:none'>
    <div class="rule"></div>

    <h3>Network Graph</h3>
    <div class="columns equacols">
      <div class="column first">
        <dl class="keyboard-mappings">
          <dt><span class="badmono">←</span> <em>or</em> h</dt>
          <dd>Scroll left</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt><span class="badmono">→</span> <em>or</em> l</dt>
          <dd>Scroll right</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt><span class="badmono">↑</span> <em>or</em> k</dt>
          <dd>Scroll up</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt><span class="badmono">↓</span> <em>or</em> j</dt>
          <dd>Scroll down</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>t</dt>
          <dd>Toggle visibility of head labels</dd>
        </dl>
      </div><!-- /.column.first -->
      <div class="column last">
        <dl class="keyboard-mappings">
          <dt>shift <span class="badmono">←</span> <em>or</em> shift h</dt>
          <dd>Scroll all the way left</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>shift <span class="badmono">→</span> <em>or</em> shift l</dt>
          <dd>Scroll all the way right</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>shift <span class="badmono">↑</span> <em>or</em> shift k</dt>
          <dd>Scroll all the way up</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>shift <span class="badmono">↓</span> <em>or</em> shift j</dt>
          <dd>Scroll all the way down</dd>
        </dl>
      </div><!-- /.column.last -->
    </div>
  </div>

  <div class="js-hidden-pane" >
    <div class="rule"></div>
    <div class="columns threecols">
      <div class="column first js-hidden-pane" >
        <h3>Source Code Browsing</h3>
        <dl class="keyboard-mappings">
          <dt>t</dt>
          <dd>Activates the file finder</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>l</dt>
          <dd>Jump to line</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>w</dt>
          <dd>Switch branch/tag</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>y</dt>
          <dd>Expand URL to its canonical form</dd>
        </dl>
      </div>
    </div>
  </div>

  <div class="js-hidden-pane" style='display:none'>
    <div class="rule"></div>
    <div class="columns threecols">
      <div class="column first">
        <h3>Browsing Commits</h3>
        <dl class="keyboard-mappings">
          <dt><span class="platform-mac">⌘</span><span class="platform-other">ctrl</span> <em>+</em> enter</dt>
          <dd>Submit comment</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>escape</dt>
          <dd>Close form</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>p</dt>
          <dd>Parent commit</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>o</dt>
          <dd>Other parent commit</dd>
        </dl>
      </div>
    </div>
  </div>

  <div class="js-hidden-pane" style='display:none'>
    <div class="rule"></div>
    <h3>Notifications</h3>

    <div class="columns threecols">
      <div class="column first">
        <dl class="keyboard-mappings">
          <dt>j</dt>
          <dd>Move selection down</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>k</dt>
          <dd>Move selection up</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>o <em>or</em> enter</dt>
          <dd>Open notification</dd>
        </dl>
      </div><!-- /.column.first -->

      <div class="column second">
        <dl class="keyboard-mappings">
          <dt>e <em>or</em> shift i <em>or</em> y</dt>
          <dd>Mark as read</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>shift m</dt>
          <dd>Mute thread</dd>
        </dl>
      </div><!-- /.column.first -->
    </div>
  </div>

</div>

    <div id="markdown-help" class="instapaper_ignore readability-extra">
  <h2>Markdown Cheat Sheet</h2>

  <div class="cheatsheet-content">

  <div class="mod">
    <div class="col">
      <h3>Format Text</h3>
      <p>Headers</p>
      <pre>
# This is an &lt;h1&gt; tag
## This is an &lt;h2&gt; tag
###### This is an &lt;h6&gt; tag</pre>
     <p>Text styles</p>
     <pre>
*This text will be italic*
_This will also be italic_
**This text will be bold**
__This will also be bold__

*You **can** combine them*
</pre>
    </div>
    <div class="col">
      <h3>Lists</h3>
      <p>Unordered</p>
      <pre>
* Item 1
* Item 2
  * Item 2a
  * Item 2b</pre>
     <p>Ordered</p>
     <pre>
1. Item 1
2. Item 2
3. Item 3
   * Item 3a
   * Item 3b</pre>
    </div>
    <div class="col">
      <h3>Miscellaneous</h3>
      <p>Images</p>
      <pre>
![GitHub Logo](/images/logo.png)
Format: ![Alt Text](url)
</pre>
     <p>Links</p>
     <pre>
http://github.com - automatic!
[GitHub](http://github.com)</pre>
<p>Blockquotes</p>
     <pre>
As Kanye West said:

> We're living the future so
> the present is our past.
</pre>
    </div>
  </div>
  <div class="rule"></div>

  <h3>Code Examples in Markdown</h3>
  <div class="col">
      <p>Syntax highlighting with <a href="http://github.github.com/github-flavored-markdown/" title="GitHub Flavored Markdown" target="_blank">GFM</a></p>
      <pre>
```javascript
function fancyAlert(arg) {
  if(arg) {
    $.facebox({div:'#foo'})
  }
}
```</pre>
    </div>
    <div class="col">
      <p>Or, indent your code 4 spaces</p>
      <pre>
Here is a Python code example
without syntax highlighting:

    def foo:
      if not bar:
        return true</pre>
    </div>
    <div class="col">
      <p>Inline code for comments</p>
      <pre>
I think you should use an
`&lt;addr&gt;` element here instead.</pre>
    </div>
  </div>

  </div>
</div>


    <div id="ajax-error-message">
      <span class="mini-icon mini-icon-exclamation"></span>
      Something went wrong with that request. Please try again.
      <a href="#" class="ajax-error-dismiss">Dismiss</a>
    </div>

    <div id="logo-popup">
      <h2>Looking for the GitHub logo?</h2>
      <ul>
        <li>
          <h4>GitHub Logo</h4>
          <a href="http://github-media-downloads.s3.amazonaws.com/GitHub_Logos.zip"><img alt="Github_logo" src="https://a248.e.akamai.net/assets.github.com/images/modules/about_page/github_logo.png?1334862345" /></a>
          <a href="http://github-media-downloads.s3.amazonaws.com/GitHub_Logos.zip" class="minibutton btn-download download">Download</a>
        </li>
        <li>
          <h4>The Octocat</h4>
          <a href="http://github-media-downloads.s3.amazonaws.com/Octocats.zip"><img alt="Octocat" src="https://a248.e.akamai.net/assets.github.com/images/modules/about_page/octocat.png?1334862345" /></a>
          <a href="http://github-media-downloads.s3.amazonaws.com/Octocats.zip" class="minibutton btn-download download">Download</a>
        </li>
      </ul>
    </div>

    
    <span id='server_response_time' data-time='0.07234' data-host='fe13'></span>
  </body>
</html>

