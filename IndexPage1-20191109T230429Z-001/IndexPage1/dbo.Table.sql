CREATE TABLE [dbo].[Table] (
    [Id]          INT           NOT NULL,
    [DocTitle]    VARCHAR (50)  NULL,
    [UploadDate]  DATE NULL,
    [DocType]     CHAR (10)     NULL,
    [Permissions] BIT     NULL,
    PRIMARY KEY CLUSTERED ([Id] ASC)
);

