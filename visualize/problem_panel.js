(function () {
  const FALLBACK = {
    "1": { slug: "two-sum", title: "Two Sum", statement: "Given nums and target, return indices of two distinct elements whose sum equals target. You may assume exactly one valid answer and cannot reuse an element." },
    "3": { slug: "longest-substring-without-repeating-characters", title: "Longest Substring Without Repeating Characters", statement: "Given a string s, return the length of the longest substring containing unique characters only." },
    "11": { slug: "container-with-most-water", title: "Container With Most Water", statement: "Given line heights, choose two lines that maximize contained water area. Return that maximum area." },
    "14": { slug: "longest-common-prefix", title: "Longest Common Prefix", statement: "Given an array of strings, return the longest common prefix among them; return empty string if no common prefix exists." },
    "20": { slug: "valid-parentheses", title: "Valid Parentheses", statement: "Given a string of bracket characters, determine whether every opening bracket is closed in correct order and type." },
    "23": { slug: "merge-k-sorted-lists", title: "Merge k Sorted Lists", statement: "Given k sorted linked lists, merge them into one sorted linked list and return its head." },
    "34": { slug: "find-first-and-last-position-of-element-in-sorted-array", title: "Find First and Last Position of Element in Sorted Array", statement: "Given sorted nums and target, return the first and last index of target; return [-1, -1] if absent." },
    "76": { slug: "minimum-window-substring", title: "Minimum Window Substring", statement: "Given s and t, return the minimum-length substring of s containing all characters of t with multiplicity." },
    "98": { slug: "validate-binary-search-tree", title: "Validate Binary Search Tree", statement: "Given a binary tree root, return true if it satisfies strict BST ordering rules for every node." },
    "102": { slug: "binary-tree-level-order-traversal", title: "Binary Tree Level Order Traversal", statement: "Given root of a binary tree, return values by breadth-first level order." },
    "104": { slug: "maximum-depth-of-binary-tree", title: "Maximum Depth of Binary Tree", statement: "Given root, return the maximum number of nodes on a path from root down to a leaf." },
    "111": { slug: "minimum-depth-of-binary-tree", title: "Minimum Depth of Binary Tree", statement: "Given root, return the shortest root-to-leaf depth." },
    "112": { slug: "path-sum", title: "Path Sum", statement: "Given root and targetSum, return true if any root-to-leaf path sums to targetSum." },
    "130": { slug: "surrounded-regions", title: "Surrounded Regions", statement: "Capture all O-regions fully surrounded by X in a board by flipping those O cells to X." },
    "133": { slug: "clone-graph", title: "Clone Graph", statement: "Given a node of a connected undirected graph, return a deep copy of the graph." },
    "141": { slug: "linked-list-cycle", title: "Linked List Cycle", statement: "Given head of linked list, determine whether a cycle exists." },
    "144": { slug: "binary-tree-preorder-traversal", title: "Binary Tree Preorder Traversal", statement: "Return preorder traversal values of a binary tree." },
    "199": { slug: "binary-tree-right-side-view", title: "Binary Tree Right Side View", statement: "Return node values visible from the right side of a binary tree." },
    "200": { slug: "number-of-islands", title: "Number of Islands", statement: "Given a grid of land and water, count connected land components (islands)." },
    "206": { slug: "reverse-linked-list", title: "Reverse Linked List", statement: "Reverse a singly linked list and return the new head." },
    "207": { slug: "course-schedule", title: "Course Schedule", statement: "Given prerequisite pairs, determine if all courses can be completed (no directed cycle)." },
    "208": { slug: "implement-trie-prefix-tree", title: "Implement Trie", statement: "Design and implement Trie with insert, search, and startsWith operations." },
    "210": { slug: "course-schedule-ii", title: "Course Schedule II", statement: "Return a valid course order satisfying prerequisites; return empty list if impossible." },
    "211": { slug: "design-add-and-search-words-data-structure", title: "Design Add and Search Words", statement: "Support addWord and search where '.' matches any single letter." },
    "212": { slug: "word-search-ii", title: "Word Search II", statement: "Find all words from a dictionary that can be formed by adjacent board cells without reuse." },
    "215": { slug: "kth-largest-element-in-an-array", title: "Kth Largest Element in an Array", statement: "Return the kth largest value in an unsorted array." },
    "261": { slug: "graph-valid-tree", title: "Graph Valid Tree", statement: "Given n and undirected edges, return true if graph is connected and acyclic." },
    "269": { slug: "alien-dictionary", title: "Alien Dictionary", statement: "Infer a valid character order from sorted words in an alien language." },
    "295": { slug: "find-median-from-data-stream", title: "Find Median from Data Stream", statement: "Support incremental insertion and median query over stream values." },
    "310": { slug: "minimum-height-trees", title: "Minimum Height Trees", statement: "Return all tree roots that produce minimum height." },
    "323": { slug: "number-of-connected-components-in-an-undirected-graph", title: "Connected Components", statement: "Count connected components in an undirected graph." },
    "347": { slug: "top-k-frequent-elements", title: "Top K Frequent Elements", statement: "Return the k most frequent elements in an array." },
    "417": { slug: "pacific-atlantic-water-flow", title: "Pacific Atlantic Water Flow", statement: "Return cells from which water can flow to both the Pacific and Atlantic boundaries." },
    "509": { slug: "fibonacci-number", title: "Fibonacci Number", statement: "Compute the nth Fibonacci number." },
    "547": { slug: "number-of-provinces", title: "Number of Provinces", statement: "Count connected components from an adjacency matrix representation." },
    "560": { slug: "subarray-sum-equals-k", title: "Subarray Sum Equals K", statement: "Count contiguous subarrays whose sum equals k." },
    "648": { slug: "replace-words", title: "Replace Words", statement: "Replace each sentence word by the shortest matching root from dictionary if available." },
    "684": { slug: "redundant-connection", title: "Redundant Connection", statement: "Find the extra edge that creates a cycle in an almost-tree undirected graph." },
    "700": { slug: "search-in-a-binary-search-tree", title: "Search in a BST", statement: "Return subtree rooted at node with value val in BST, else null." },
    "701": { slug: "insert-into-a-binary-search-tree", title: "Insert into a BST", statement: "Insert value into BST while preserving BST ordering and return root." },
    "704": { slug: "binary-search", title: "Binary Search", statement: "Return index of target in sorted array, else -1." },
    "721": { slug: "accounts-merge", title: "Accounts Merge", statement: "Merge accounts that share emails and return grouped sorted emails with owner name." },
    "739": { slug: "daily-temperatures", title: "Daily Temperatures", statement: "For each day, return days until a warmer temperature; 0 if none." },
    "743": { slug: "network-delay-time", title: "Network Delay Time", statement: "Given weighted directed edges, find time for signal from k to reach all nodes, else -1." },
    "778": { slug: "swim-in-rising-water", title: "Swim in Rising Water", statement: "Find minimum time t to travel from top-left to bottom-right in elevation grid." },
    "787": { slug: "cheapest-flights-within-k-stops", title: "Cheapest Flights Within K Stops", statement: "Find cheapest path from src to dst using at most k stops, or -1 if impossible." },
    "933": { slug: "number-of-recent-calls", title: "Number of Recent Calls", statement: "Implement RecentCounter to return number of requests in last 3000 ms." },
    "1046": { slug: "last-stone-weight", title: "Last Stone Weight", statement: "Repeatedly smash two heaviest stones and return final weight or 0." },
    "1136": { slug: "parallel-courses", title: "Parallel Courses", statement: "Return minimum semesters to complete all courses with prerequisites, or -1 if impossible." },
    "1334": { slug: "find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance", title: "Find the City With the Smallest Number of Neighbors", statement: "Return city with fewest reachable nodes within threshold distance; break ties by larger index." },
    "1631": { slug: "path-with-minimum-effort", title: "Path With Minimum Effort", statement: "Find path minimizing maximum absolute height difference between consecutive cells." }
  };

  function getProblemId() {
    const titleMatch = (document.title || "").match(/LC\s*#\s*(\d+)/i);
    if (titleMatch) return titleMatch[1];
    const h1 = document.querySelector(".header-left h1") || document.querySelector("h1");
    if (!h1) return "";
    const h1Match = (h1.textContent || "").match(/LC\s*#\s*(\d+)/i);
    return h1Match ? h1Match[1] : "";
  }

  function getProblemTitle() {
    const h1 = document.querySelector(".header-left h1") || document.querySelector("h1");
    if (!h1) return "LeetCode Problem";
    return (h1.textContent || "LeetCode Problem").replace(/\s+/g, " ").trim();
  }

  function getProblemStatement() {
    const p = document.querySelector(".header-left p");
    if (p && p.textContent) return p.textContent.trim();
    return "Practice prompt is available in this visualization. Use this panel as quick reference while solving.";
  }

  function mdToText(md) {
    return md
      .replace(/```[\s\S]*?```/g, function (block) {
        return "\n" + block.replace(/```/g, "").trim() + "\n";
      })
      .replace(/\*\*(.*?)\*\*/g, "$1")
      .replace(/`([^`]+)`/g, "$1")
      .replace(/\[(.*?)\]\((.*?)\)/g, "$1")
      .replace(/^\s*[-*]\s+/gm, "- ")
      .replace(/^\s*#{1,6}\s*/gm, "")
      .replace(/\n{3,}/g, "\n\n")
      .trim();
  }

  function extractProblemSection(readmeText, id) {
    const lines = readmeText.split(/\r?\n/);
    const idNeedle = "#" + id;
    let start = -1;
    for (let i = 0; i < lines.length; i++) {
      if (lines[i].includes("**LeetCode**") && lines[i].includes(idNeedle)) {
        // Capture from nearest preceding heading (usually "### Problem X")
        start = i;
        for (let j = i; j >= 0 && j >= i - 4; j--) {
          if (/^###\s+Problem/i.test(lines[j].trim())) { start = j; break; }
        }
        break;
      }
    }
    if (start === -1) return "";

    let end = lines.length;
    for (let i = start + 1; i < lines.length; i++) {
      const t = lines[i].trim();
      if (/^###\s+Problem/i.test(t) || t === "---") {
        end = i;
        break;
      }
    }
    const section = lines.slice(start, end).join("\n");
    return mdToText(section);
  }

  async function loadDetailedStatement(id) {
    try {
      const res = await fetch("../README.md", { cache: "no-store" });
      if (!res.ok) return "";
      const md = await res.text();
      return extractProblemSection(md, id);
    } catch (e) {
      return "";
    }
  }

  function addStyle() {
    const style = document.createElement("style");
    style.textContent =
      ".pp-open-btn{position:fixed;right:16px;bottom:16px;z-index:10000;background:#1c3458;border:1px solid #58a6ff;color:#58a6ff;padding:8px 12px;border-radius:8px;font:600 12px/1 -apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;cursor:pointer}" +
      ".pp-overlay{position:fixed;inset:0;background:rgba(0,0,0,.45);z-index:10001;display:none}" +
      ".pp-overlay.show{display:block}" +
      ".pp-panel{position:absolute;top:0;right:0;width:min(560px,92vw);height:100%;background:#161b22;border-left:1px solid #30363d;display:flex;flex-direction:column}" +
      ".pp-head{display:flex;justify-content:space-between;gap:10px;padding:14px;border-bottom:1px solid #30363d}" +
      ".pp-title{font:700 16px/1.3 -apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;color:#f0f6fc}" +
      ".pp-sub{margin-top:6px;font:500 11px/1.3 -apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;color:#8b949e}" +
      ".pp-close{background:transparent;border:1px solid #30363d;color:#c9d1d9;border-radius:6px;padding:5px 9px;font:700 12px/1 -apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;cursor:pointer}" +
      ".pp-body{padding:14px;overflow:auto}" +
      ".pp-text{white-space:pre-wrap;font:500 13px/1.55 -apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;color:#c9d1d9}";
    document.head.appendChild(style);
  }

  async function createPanel() {
    const id = getProblemId();
    const title = getProblemTitle();
    const fallback = id && FALLBACK[id] ? FALLBACK[id] : null;
    let statement = getProblemStatement();
    const detailed = id ? await loadDetailedStatement(id) : "";
    if (detailed) statement = detailed;
    else if (fallback && fallback.statement) statement = fallback.statement;

    const btn = document.createElement("button");
    btn.className = "pp-open-btn";
    btn.type = "button";
    btn.textContent = "Problem";

    const overlay = document.createElement("div");
    overlay.className = "pp-overlay";
    overlay.innerHTML =
      '<aside class="pp-panel" role="dialog" aria-label="Problem statement">' +
      '  <div class="pp-head">' +
      '    <div>' +
      '      <div class="pp-title"></div>' +
      '      <div class="pp-sub"></div>' +
      '    </div>' +
      '    <button type="button" class="pp-close">Close</button>' +
      '  </div>' +
      '  <div class="pp-body"><div class="pp-text"></div></div>' +
      '</aside>';

    const titleEl = overlay.querySelector(".pp-title");
    const subEl = overlay.querySelector(".pp-sub");
    const textEl = overlay.querySelector(".pp-text");
    if (titleEl) titleEl.textContent = title;
    if (subEl) {
      const sub = id ? "LC #" + id : "LeetCode problem";
      subEl.textContent = detailed ? sub + " · detailed local statement" : sub + " · quick fallback";
    }
    if (textEl) textEl.textContent = statement;

    if (fallback && fallback.slug && id) {
      const head = overlay.querySelector(".pp-head > div");
      if (head) {
        const link = document.createElement("a");
        link.href = "https://leetcode.com/problems/" + fallback.slug + "/";
        link.target = "_blank";
        link.rel = "noopener noreferrer";
        link.style.cssText = "display:inline-block;margin-top:6px;font:600 11px/1.2 -apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;color:#58a6ff;text-decoration:none";
        link.textContent = "Open official LeetCode page";
        head.appendChild(link);
      }
    }

    function openPanel() { overlay.classList.add("show"); }
    function closePanel() { overlay.classList.remove("show"); }

    btn.addEventListener("click", openPanel);
    const closeBtn = overlay.querySelector(".pp-close");
    if (closeBtn) closeBtn.addEventListener("click", closePanel);
    overlay.addEventListener("click", function (e) { if (e.target === overlay) closePanel(); });
    document.addEventListener("keydown", function (e) { if (e.key === "Escape") closePanel(); });

    document.body.appendChild(btn);
    document.body.appendChild(overlay);
  }

  async function start() {
    if (!document.body || !document.head) return;
    addStyle();
    await createPanel();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", start);
  } else {
    start();
  }
})();
