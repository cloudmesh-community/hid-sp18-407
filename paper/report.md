# :o: Title missing

:o: author missing

:o: look at other students examples how to do that

:o: as in original latex the sections are inconsistent

:o: as in original latex all cistations are wrong as the start with a
period and end with a period. However citations must be enclosed
within the sentence. This is the same as in other academic fields.

:o: CONVERT THIS TO MD:

```
\def\paperchapter{Apache Kudu} % This section is typically a single keyword. from
                   % a small list. Consult with theinstructors about
                   % yours. They typically fill it out once your first
                   % text has been reviewed.
\def\hid{hid-sp18-407} % all hids of the authors of this
                                % paper. The paper must only be in one
                                % authors directory and all other
                                % authors contribute to it in that
                                % directory. That authors hid must be
                                % listed first
\def\volume{9} % the volume of the proceedings in which this paper is to
           % be included

\def\locator{\hid, Volume: \volume, Chapter: \paperchapter, Status: \paperstatus. \newline}

\title{Processing Massive Datasets: Apache Kudu and Cloudera Impala}

\author{Keith Hickman}
\affiliation{%
  \institution{Indiana University School of Informatics and Computing}
  \streetaddress{919 E 10th St}
  \city{Bloomington} 
  \state{Indiana} 
  \postcode{47408}
}
\email{keonhick@iu.edu}
```

## Introduction

The evolution of cloud computing technologies changes at an
ever-increasing pace. Applications of these technologies vary greatly
but have one thing in common: the need to ingest, store, process,
manipulate, and extract substantial amounts of data with which to make
decisions. The volume of these available data has increased just as
quickly, as organizations increasingly view data as a commodity and
asset. One effect of this trend is the shift of focus away from some
well-established technologies toward new methods aimed at scalable
processing power. [@hid-sp18-kudu-intro].

#### Background

SQL was the dominiant language for working with data until the
mid-2000's. With the explosion in the volume and velocity of available
data, programmers struggled to scale SQL-based storage and query engines
to meet demand; thus NoSQL and schema-less data was born. The
write-once, read-many data stores provided several advantages over
relational data stores, including speed and flexibility. Now, Relational
Database Management Systems (RDBMS) platforms are coming back into favor
once again as processing power overcomes the hurdles for which NoSQL was
originally designed. Many of the reasons that contributed to the decline
of RDBMS became unpopular and are no longer relevant, or the problems
have been solved. Developers can now choose a programming paradigm
depending on their specific needs without sacrificing performance or
usability, and without having to create complex architectures. Kudu
represents one option in this domain. In 2015, Cloudera donated the Kudu
project to the Apache Software Foundation in hopes that a full-time
developer community would spark the projects into stable, widely adopted
platforms. [@hid-sp18-407-cloudera-donates].

## Kudu

Kudu was started in 2014 and is now a Top-Level Project within Apache.
Driven by need to ingest, update, and analyze massive datasets at scale,
given a low-cost, open-source framework, Kudu is described as an
open-source storage engine for structured data designed to provide
low-latency random access to distributed data sources, particularly
within the Hadoop ecosystem.  [@hid-sp18-407-kudu-intro]. "At a high
level, Kudu is a new storage manager that enables durable single-record
inserts, updates, and deletes, as well as fast and efficient columnar
scans due to its in-memory row format and on-disk columnar format."
 [@hid-sp18-407-kudu-impala-integration]. One of the main advantages
Kudu offers is a simple API for row-level writes, updates, upserts, and
deletes, while maintaining query throughput speeds similar to binary
stores such as Apache Avro. [@hid-sp18-407-kudu-intro].

## Kudu's Design

Kudu benefits from several design choices aimed at bridging the gap
between static and dynamic data stores. Static Hadoop data stores such
as Apache Avro or Parquet have limited ability to write which gives
low-latency interactivity. These "traditional" data management stores in
represent immutable databases and are more suited to unstructured or
semi-structured streaming data. [@hid-sp18-407-kudu-intro]. Whereas
semi or unstructured stores such as Hive can read and write real-time
data but provide less-than-optimal analytical performance.
 [@hid-sp18-407-impala-intro]. Mutable databases like Hive and Hbase
allow for low-latency record-level reads and writes, but lag behind the
static file formats for applications like SQL-based analytics and
machine learning.  [@hid-sp18-407-kudu-impala-integration]. "Kudu fills
the gap between immutability in static data stores and latency during
sequential read-through in mutable databases, and offers several
improvements and design choices in read, write, distribution, and
maintenance operations."  [@hid-sp18-407-impala-intro]. This is shown in
Figure 1  [1](#f:kudu){reference-type="ref" reference="f:kudu"}.


TODO: IMAGES DIR MUST BE IN THIS FOLDER

![Kudu Graph[]{label="f:kudu"}](images/kudu.png){#f:kudu
width="\columnwidth"}

#### Hadoop Ecosystem

Kudu is designed as a tightly integrated data store in the Hadoop
ecosystem. Accordingly, the platform works well with any of the Hadoop
technologies, including Impala, which is a high-performance SQL query
platform also incubated and developed by Apache.
 [@hid-sp18-407-impala-intro]. Kudu and Impala together provide many
advantages. With Kudu, a user can access many data stores through a
single query engine like Impala. With Impala, many sources of data can
be queried from a single SQL interface, such as Hive, Hbase, or
naturally Kudu. Kudu is tightly integrated with Impala which supports
the entire Apache ecosystem including Spark, Hive, Hbase, and others.
 [@hid-sp18-407-benchmarking-kudu]. Because both platforms are part of
the Hadoop ecosystem, their capabilities are greatly expanded through
interoperability with the data stores, cluster managers, and
visualization tools.

#### Kudu vs. Lambda Architecture

This architecture makes Kudu very attractive for storing streaming data
that may need to be modified at a later time, such as healthcare
monitoring, weather data, or any application that requires real-time
analytical and row-level update performance.
 [@hid-sp18-407-kudu-schema-design]. "Today, many users try to solve
this challenge via a Lambda architecture, which presents inherent
challenges by requiring different code bases and storage for the
necessary batch and real-time components."
 [@hid-sp18-407-kudu-impala-integration] Using Kudu and Impala together
circumvents the need for such complex architecures, as they are
well-suited for real-time interactivity and are designed to be tightly
integrated.

#### Flexible Horizontal Partionioning Schemes

Kudu utilizes a flexible array of horizontal partitioning schemes to
achieve high-throughput storage and low-latency random access.
 [@hid-sp18-407-kudu-intro] Contrast other distributed data stores such
as Hbase or Cassandra which use only one of either key-range horizontal
partitioning, or hash partition methods respectively. In Kudu, "the
partition schema acts as a function which can map from a primary key
tuple into a binary partition key. Each tablet covers a contiguous range
of these partition keys. Thus, a client, when performing a read or
write, can easily determine which tablet should hold the given key and
route the request accordingly."  [@hid-sp18-407-kudu-intro] By
optimizing the scanning features and compression codecs, Kudu reduces
the amount of time needed to return row-level data. Additionally, the
flexibility of choosing the appropriate partitioning scheme makes Kudu
an viable option for high-throughput scenarios such as real-time
healthcare data, sports broadcasting, weather, or any other analytical
application that require near-real-time information.

Tablet Storage Goals: 1. Fast Columnar scans 2. Low-latency random
updates 3. Consistency of performance.

#### Raft

Kudu uses the Raft consensus method and horizontal partitioning of
tables into "tablets" or the subset of a partitioned table. Conversely,
Parquet, a static binary data store, uses vertical partitioning, which
can provide performance advantages in partial queries and retrievals.
 [@hid-sp18-407-benchmarking-kudu]. Raft implements consensus by first
electing a distinguished leader, then giving the leader complete
responsibility for managing the replicated log. The leader accepts log
entries from clients, replicates them on other servers, and tells
servers when it is safe to apply log entries to their state machines.
 [@hid-sp18-407-raft-algo]. Having a leader simplifies the management of
the replicated log. For example, the leader can decide where to place
new entries in the log without consulting other servers, and data flows
in a simple fashion from the leader to other servers. A leader can fail
or become disconnected from the other servers, in which case a new
leader is elected.  [@hid-sp18-407-raft-algo]. Note, the concept of a
leader:follower is different than a master:client relationship in
Hadoop. Kudu improves upon the Raft algorithm in two ways: first by
using an exponential back-off algorithm to avoid data packet collisions
after a failed leader election. Essentially, the backoff algorithm works
by randomly choosing increasing time delay values for clients to send
data until there is no longer a conflict. Second, "when a new leader
contacts a client whose log diverges from its own, Raft proposes
iteratively stepping backward until the point where the two logs
diverge. Kudu proposes immediately jumping back to the last
committedIndex, potentially saving many steps."
 [@hid-sp18-407-kudu-intro].

#### Mutability

INSERT and ALTER TABLE operations are the primary advantage Kudu has
over non-relational, or NoSQL databases like Hbase or Cassandra. The
immutability of NoSQL databases provides significant performance
advatages over traditional RDBMS, but at the expense of write
capabilities. The converse is true for traditional relational databases.
Kudu fills this gap, offering lower-latency benchmarked performance over
relational databases such as MySQL, and writability-upon-ingestion not
found in NoSQL databases. "If a client wishes to write, it first locates
the leader replica and sends a write request to that replica. If that
replica is no longer the leader, the request will error out, the replica
will refresh its metadata cache, and a new request will be resent to the
new leader."  [@hid-sp18-407-kudu-intro] While this process may seem
cumbersome or error-prone, Kudu's robust scheduling manager is designed
with fault-tolerance and performance in mind. Obviously recording the
correct order of the entries is paramount, which Kudu accomplishes with
a local lock manager. "If a majority of the followers accept the write
and log it to their own local write-ahead logs, the write it considered
durably replicated."  [@hid-sp18-407-kudu-intro].

#### Schema Design

Kudu takes advantage of strongly-typed columns. As such, users must
specify the desired column type versus using a schema-less table as in a
NoSQL database. This provides the advantage of Kudu feeling and acting
in many ways like a familiar relational database, while allowing for
improved read-write performance over NoSQL databases.
 [@hid-sp18-407-kudu-schema-design].

## Encoding

Columns can be encoded depending on the type in one of five ways: plain,
bitshuffle, run length, prefix, and dictionary. Plain encoding is data
stored in its natural format, whereas bitshuffle arranges a data array
into a matrix and then transposes that matrix, keeping only the most
significant bits.  [@hid-sp18-407-bitshuffle].

## Security


Security and encryption are two concerns and something that Kudu team
treats seriously. Kudu uses Hadoop security roles and permissions via
Kerberos authentication. As of the date of this writing, Kudu also
integrates with Apache Sentry, which provides role-based authentication
methods. "System-wide security is supported for Kudu API calls, but one
can still use Apache Sentry with Impala to secure Kudu tables for the
end users."  [@hid-sp18-407-benchmarking-kudu]. Kudu has been tested to
support common encryption software, but this area may leave somewhat of
a gap.

## Conclusion

:o: the term sum means something else and should be avoided, is it not summary?

In sum, Kudu presents a modern, efficient distributed data store that
bridges an existing gap between static, real-time access data stores and
mutable, high-latent data stores. Given the compatibility with
next-generation hardware such as solid-state drives, Kudu has the
potential to become an increasingly useful solution and drive the
re-emergence of relational database management systems.

The author would like to thank Dr. Gregor von Laszewski for his support
and suggestions to write this paper.

