<!--
 * @Author: KivenChen
 * @Date: 2019-04-19
 -->

https://leetcode-cn.com/api/problems/all/

记录了用户解决问题的分布以及所有问题的基本信息

GET 即可，需要设置 cookie

cookie 由登陆账号后获取：https://leetcode-cn.com/accounts/login/

包含以下信息：

- ac_easy
- ac_hard
- ac_medium
- num_solved
- num_total
- stat_status_pairs.status
- stat_status_pairs.is_favor
- stat_status_pairs.paid_only
- stat_status_pairs.difficulty.level
- stat_status_pairs.stat.question_id
- stat_status_pairs.stat.frontend_question_id
- stat_status_pairs.stat.question__title
- stat_status_pairs.stat.question__title_slug
- stat_status_pairs.stat.questuon__article__live
- stat_status_pairs.stat.question__article__slug
- stat_status_pairs.stat.is_new_question
- stat_status_pairs.stat.total_acs
- stat_status_pairs.stat.total_submitted

官方解答：https://leetcode-cn.com/articles/{question__article__slug}

仅提供链接

https://leetcode-cn.com/graphql

POST 得到响应，需提供以下信息：

- operationName
- query
- variables

如果 
operationName: "questionData"
query: "query questionData($titleSlug: String!) {↵  question(titleSlug: $titleSlug) {↵    questionId↵    questionFrontendId↵    boundTopicId↵    title↵    titleSlug↵    content↵    translatedTitle↵    translatedContent↵    isPaidOnly↵    difficulty↵    likes↵    dislikes↵    isLiked↵    similarQuestions↵    contributors {↵      username↵      profileUrl↵      avatarUrl↵      __typename↵    }↵    langToValidPlayground↵    topicTags {↵      name↵      slug↵      translatedName↵      __typename↵    }↵    companyTagStats↵    codeSnippets {↵      lang↵      langSlug↵      code↵      __typename↵    }↵    stats↵    hints↵    solution {↵      id↵      canSeeDetail↵      __typename↵    }↵    status↵    sampleTestCase↵    metaData↵    judgerAvailable↵    judgeType↵    mysqlSchemas↵    enableRunCode↵    enableTestMode↵    envInfo↵    __typename↵  }↵}↵"
variables: {titleSlug: "number-of-enclaves"}

记录了给定问题的相关信息

包含以下信息：

- data.question.content
- data.question.hints
- data.question.difficulty
- data.question.isPaidOnly
- data.question.langToValidPlayground
- data.question.questionId
- data.question.questionFrontendId
- data.question.similarQuestions
- data.question.status
- data.question.title
- data.question.titleSlug
- data.question.translatedContent
- data.question.translatedTitle
- data.question.stats
- data.question.topicTags

跳转至原问题网页：https://leetcode-cn.com/problems/{titileSlug}

https://leetcode-cn.com/submissions/latest/?qid={questionId}&lang={lang}

获取最新提交的解答

如果
operationName: "Submissions"
query: "query Submissions($offset: Int!, $limit: Int!, $lastKey: String, $questionSlug: String!) {↵  submissionList(offset: $offset, limit: $limit, lastKey: $lastKey, questionSlug: $questionSlug) {↵    lastKey↵    hasNext↵    submissions {↵      id↵      statusDisplay↵      lang↵      runtime↵      timestamp↵      url↵      isPending↵      memory↵      __typename↵    }↵    __typename↵  }↵}↵"
variables: {offset: 0, limit: 20, lastKey: null, questionSlug: "friends-of-appropriate-ages"}

记录了提交的代码信息

包含：

- data.submissionList.submissions.lang
- data.submissionList.submissions.memory
- data.submissionList.submissions.runtime
- data.submissionList.submissions.statusDisplay
- data.submissionList.submissions.timestamp
- data.submissionList.submissions.url


如果
operationName: null
query: "{↵  brightTitle↵  allContests {↵    containsPremium↵    title↵    cardImg↵    titleSlug↵    description↵    startTime↵    duration↵    originStartTime↵    isVirtual↵    company {↵      watermark↵      __typename↵    }↵    __typename↵  }↵}↵"
variables: {}

记录了所有竞赛的信息

包含：

- data.allContests.title
- data.allContests.titleSlug

竞赛链接：https://leetcode-cn.com/contest/api/ranking/weekly-contest-132/?pagination=1&region=local


如果
operationName: "contestGroup"
query: "query contestGroup($slug: String!) {↵  contestGroup(slug: $slug) {↵    title↵    contestCount↵    contests {↵      title↵      titleSlug↵      startTime↵      duration↵      questions {↵        title↵        titleCn↵        titleSlug↵        credit↵        __typename↵      }↵      __typename↵    }↵    __typename↵  }↵}↵"
variables: {slug: "2019-spring"}

记录了2019春季赛的信息

包含：

- data.contestGroup.contests.title
- data.contestGroup.contests.titleSlug
- data.contestGroup.contests.question.title
- data.contestGroup.contests.question.titleCn
- data.contestGroup.contests.question.titleSlug