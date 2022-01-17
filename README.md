# FlagWaverBotReborn

## Summoning

To summon the bot on a subreddit where it has been permitted access by
the moderators you can type `!wave` in a comment to generate links from
the post or comment you are replying to or `!wavethis` in a comment
or text post to generate links in you own comment or post.

These can be combined in one comment to wave links in it and its parent.

On any other subreddit you will need to ping the bot for it to respond.
`!wave` and/or `!wavethis` is still needed, and the bot cannot see mentions
in text posts or comments with more than four mentions.

### What can the bot process?

The bot understands

- Direct image link (images that open directly in the browser, if the url has a .jpg/.png in it it's likely good)
- Reddit galleries
- Imgur image links (imgur.com/abc123)
- Imgur album links (imgur.com/a/abc123)

## There's a problem with the bot/I have a suggestion for the bot

First, make sure that the problem/suggestion is with/for the bot, not the website.
This bot has nothing to do with the website and matters with the website
go [here](https://github.com/krikienoid/flagwaver).

### Error
To report an error go [here](https://github.com/LunarRequiem/FlagWaverBotReborn/issues/new?assignees=&labels=bug&template=bug_report.md&title=).

If you received an error message from the bot, please link it.

If the bot was not summoned please link where you tried to summon it.

If the bot was summoned but the link provided is wrong, please link the message.

If none of these are provided I cannot help you at all.

### Suggestion

To suggest an improvement go [here](https://github.com/LunarRequiem/FlagWaverBotReborn/issues/new?assignees=&labels=enhancement&template=feature_request.md&title=)

## Running the bot

To run the bot yourself you need to set up a [reddit bot account](https://www.reddit.com/wiki/api)
and type the keys, username, and password in `/secret.yaml`

Optionally you can also have Imgur support, which requires an [Imgur API key](https://api.imgur.com/oauth2/addclient)
(only the public key is needed). Without this the bot cannot understand Imgur
Albums or indirect image links. If you do not want imgur support you must set `use_imgur: false`
in `settings.yaml`

## I am a moderator of a subreddit and would like the bot on my subreddit

Please send modmail to /u/Lunar_Requiem, as I need to know that the 
request came from a mod 
