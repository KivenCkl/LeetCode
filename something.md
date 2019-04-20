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

如果 operationName 为 questionData，variables 为 titleSlug: {titleSlug}

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

如果 operationName 为 Submissions，variables 为 questionSlug: {titleSlug}

记录了提交的代码信息

包含：

- data.submissionList.submissions.lang
- data.submissionList.submissions.memory
- data.submissionList.submissions.runtime
- data.submissionList.submissions.statusDisplay
- data.submissionList.submissions.timestamp
- data.submissionList.submissions.url