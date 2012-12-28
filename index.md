> This page is *about* the Dendrite Network, to actually *use* the Dendrite Network go to http://dendritenetwork.com/

### Behind the Scenes
This page describes the concepts and operation of the system. If something is unclear after reading this document consider asking about it on the [Dendrite Network Google Group](https://groups.google.com/d/forum/dendrite-network).

If you're viewing this page via a *bump URL* you will see a header with three buttons on the left, *Engage*, *Forward*, and *Reject*, and a link to visit the sender of the *bump URL*.  And on the right you'll see an *Explain* button.

If you're *not* viewing this page via a *bump URL* but would like to you can [just click here to try it](http://dendritenetwork.com/bump/tlpa3gx03bh7docieg448ca5/ns0kskob8jyx3y998j4a68hl/).  You'll be brought to a page to choose your own *avatar* URL (see below) and then, once you've done that, you'll be brought back here but under a *bump URL* header.

### What?
The Dendrite Network is a simple way to spread an idea (or *meme*) and track the spread.

The idea takes the form of an URL.  In other words, you can spread the word about any website.

You and the people who participate in the D.N. also identify yourselves with an URL called an *avatar URL*.  Again, this can be any page on the web, but if you want to be contacted then obviously it should be a page that includes some means of contacting you.

When you have chosen an *avatar URL* and picked an URL to propagate, you [enter them in the Dendrite Network homepage](http://dendritenetwork.com/) and generate a *bump URL*.  (The D.N. sets a cookie to remember your *bump URL* for you so you don't have to re-enter it next time you visit, but you can change it at any time from the [D.N. home page](http://dendritenetwork.com/).)

Once you have the *bump URL* you spread it around, send it to some friends and explain a little about what's going on.  When they visit the URL they'll see the same "choose your own *avatar URL*" page you saw, and they'll have the option from there to pick an *avatar URL* of their own or simply go directly to the page that you're propagating.

As your friends repeat the process, picking their own *avatar URLs*, propagating *bump URLs*  to their friends, who then repeat the process again, etc..., a *graph* begins to be built up in the D.N. log showing the spread of the idea from person to person.

### Why?
I created the D.N. to provide a simple convenient way for normal everyday people to earn income from the Internet.  The D.N. itself is a personal project, not a commercial concern, and it will never become commercial.  If it takes off I'll start a non-profit to administer it.

So, if the D.N. is non-commercial, how are people going to use it to earn income?

### How?
The D.N. forms a neutral *platform* for specific campaigns people run on top of it.  Anyone with something to sell or promote can use the D.N. to do it and watch the resulting graph of word-of-mouth connection growing in near-real-time.

It is up to the individual campaign-runners to figure out how to reward their network members for spreading the word.  This is just like Kickstarter or IndieGoGo where the project sponsors must create a schema of rewards for their investor/benefactors.

Once you have a plan to reward people for spreading your idea you simply publish it and start spreading your *bump URL*.  You can track the spread of the idea in the D.N. log and I'll be writing up some tools for generating fancy graph images and such soon.

### Goodies and Future Plans
In addition to the main function of spreading ideas and tracking the spread, the D.N. also provides for feedback from the people spreading the ideas to the originators of those ideas.

In addition to the (default) action of *Forward*, there are two other actions (buttons) in the *bump URL* header: *Engage* and *Reject*.

If you click *Engage* two things happen: a note of that action is made in the D.N. log and then your are redirected *directly to the meme URL*.  Basically you are indicating that you want to *engage* with the site or idea.  If it is a commercial product that likely means you want to purchase it, or at least learn more.  It could also be a petition that you want to sign, or a service that you decide to join, whatever.  Clicking *Engage* means you want to engage with it.

If you click *Reject* you will have the chance to enter a brief *reason* in a drop down dialog window and *post that reason for your rejection to the D.N. log*.  Everyone, including the originator, will be able to see it.

Alls "bumps", "engages" and rejections appear in the publicly-viewable D.N. log so the system is completely transparent to all the users.

Furthermore, because you are only sending and receiving *bump URLs* to and from *people you know* there won't be any spam!  Think about it: you wouldn't forward spam to your friends, would you? If you wanted to stay friends with them, that is?

And if someone does send you something you're not interested in or that you find disagreeable you can post a rejection notice saying why.

This is still very much an experiment and I am just starting out.  I intend to hold some classes for [another project of mine](http://thinkpigeon.blogspot.com/?view=mosaic) and I am using the D.N. to spread teh word about it it, so I will let you know how it goes (watch this space or [join the mailing list!](https://groups.google.com/d/forum/dendrite-network))

I'm also going to set up BitTorrent for the log(s) to ease traffic (I should be so lucky!) if a lot of people are trying to view the graphs and activity, and I want to create some useful tools for running campaigns and tracking and rewarding spread and engagement.


### Development and Source Code
The Dendrite Network is open source under the GPL (v3).  If you would like to help out on the internals of the system or just have look at the source code [it's hosted on Github](https://github.com/PhoenixBureau/DendNet). You'll see that the Dendrite Network is actually very simple in operation.  Most of the action takes place in the user's browser, the server is very simple and does little more than save events to a log and the internal database.

The real action is in the network visualization tools.  I plan to make something cool with [NetworkX](http://networkx.lanl.gov/) soon.


Thank you very much,
Warm regards,
Simon Forman (@calroc on Github)

