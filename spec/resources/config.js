async function loadTurtle() {
    //this is the function you call in 'preProcess', to load the highlighter
    const worker = await new Promise(resolve => {
        require(["core/worker"], ({ worker }) => resolve(worker));
    });
    const action = "highlight-load-lang";
    const langURL =
        "https://cdn.jsdelivr.net/gh/redmer/highlightjs-turtle/src/languages/turtle.js";
    const propName = "hljsDefineTurtle"; // This funtion is defined in the highlighter being loaded
    const lang = "turtle"; // this is the class you use to identify the language
    worker.postMessage({ action, langURL, propName, lang });
    return new Promise(resolve => {
        worker.addEventListener("message", function listener({ data }) {
            const { action: responseAction, lang: responseLang } = data;
            if (responseAction === action && responseLang === lang) {
                worker.removeEventListener("message", listener);
                resolve();
            }
        });
    });
}

var respecConfig = {
    // check https://respec.org/docs/ for the meaning of these keys
    preProcess: [loadTurtle],
    prevVersion: "https://kg-construct.github.io/rml-fnml/spec/docs/20260202/",
    authors: [
        {
            name: "Ben De Meester",
            company: "Ghent University &ndash; imec &ndash; IDLab",
            url: "https://ben.de-meester.org/#me",
            orcid: "0000-0003-0248-0987",
            companyURL: "https://knows.idlab.ugent.be/"
        },
        {
            name: "Samaneh Jozashoori",
            company: "metaphacts",
            url: "https://scholar.google.com/citations?user=7gXRi3YAAAAJ",
            orcid: "0000-0003-1702-8707",
            companyURL: "https://metaphacts.com/"
        },
        {
              name: "Pano Maria",
              company: "ModelDesk",
              url: "https://modeldesk.io",
              orcid: "0009-0000-2598-1894",
              companyURL: "https://modeldesk.io"
        },
        {
              name: "David Chaves-Fraga",
              url: "https://davidchavesfraga.com",
              company: "CiTIUS &ndash; University of Santiago de Compostela",
              orcid: "0000-0003-3236-2789",
              companyURL: "https://citius.gal"
            },
         {
              name: "Anastasia Dimou",
              mailto: "anastasia.dimou@kuleuven.be",
              company: "KU Leuven",
              orcid: "0000-0003-2138-7972",
              companyURL: "https://dtai.cs.kuleuven.be/"
       },
    ],
    edDraftURI: "https://w3id.org/rml/fnml/spec/",
    editors: [
        {
            name: "Ben De Meester",
            company: "Ghent University &ndash; imec &ndash; IDLab",
            url: "https://ben.de-meester.org/#me",
            orcid: "0000-0003-0248-0987",
            companyURL: "https://knows.idlab.ugent.be/"
        }
    ],
    formerEditors: [
       {
              name: "Anastasia Dimou",
              mailto: "anastasia.dimou@kuleuven.be",
              company: "KU Leuven",
              orcid: "0000-0003-2138-7972",
              companyURL: "https://dtai.cs.kuleuven.be/"
       }
    ],
    github: "https://github.com/kg-construct/rml-fnml",
    latestVersion: null,
    license: "w3c-software-doc",
    localBiblio: {
        RML: {
            title: "RDF Mapping Language (RML)",
            href: "https://rml.io/specs/rml/",
            status: "Unofficial Draft",
            publisher: "IDLab - imec - Ghent University",
            date: "08 October 2020",
        },
        FnO: {
            title: "Function Ontology (FnO)",
            href: "https://w3id.org/function/spec/",
            status: "Unofficial Draft",
            publisher: "IDLab - imec - Ghent University",
            date: "10 November 2021",
        },
        CollectionsContainers: {
            title: "Collections and Containers in RML",
            href: "https://w3id.org/kg-construct/collections-containers",
            status: "Unofficial Draft",
            publisher: "Knowledge Graph Construction W3C Community Group ",
            date: "16 August 2022",
        },
    },

    // shortName: "RML-FNML",
    specStatus: "CG-DRAFT",
    // W3C config
    copyrightStart: "2021",
    doJsonLd: true,
    group: "kg-construct",
};